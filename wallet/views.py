import decimal
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import generics, response, status
from rest_framework.renderers import JSONRenderer
from .serializer import TransferSerializer, ActionsListSerializer
from custom_auth.models import User
from .models import Wallet
from rest_framework import decorators
from .currency import get_currency
from currency_converter import CurrencyConverter
from actions.utils import create_action
from actions.models import Actions

c = CurrencyConverter(decimal=True)


@decorators.api_view(['GET', 'POST'])
@decorators.renderer_classes([JSONRenderer,])
def transfer(request):
    serializer = TransferSerializer()
    serializer = TransferSerializer(data=request.data)
    if serializer.is_valid():
        try:
            cd = serializer.data
            receiver = User.objects.get(email=cd['to_email'])
            receiver = Wallet.objects.get(user=receiver)
            sender = Wallet.objects.get(user=request.user)
            qwe = sender.balance - decimal.Decimal(cd['how_much'])
            sender.balance -= decimal.Decimal(cd['how_much'])
            if sender.balance < 0:
                raise Exception('balance cannot be less than zero')
            else:
                create_action(sender.user,
                              f'money transfer in the ammount {cd["how_much"], sender.currency} to {receiver.user}'
                              , receiver.user)
                sender.save()
            if sender.currency == receiver.currency:
                receiver.balance += decimal.Decimal(float(cd['how_much']))
                receiver.save()
                sender.save()
                return response.Response('IF WAS WORKED', status=status.HTTP_202_ACCEPTED)
            else:
                summ = c.convert(float(cd['how_much']), sender.currency, receiver.currency)
                receiver.balance += summ
                receiver.save()
                sender.save()
                return response.Response('ELSE WORKED', status=status.HTTP_202_ACCEPTED)
        except ObjectDoesNotExist:
            return response.Response('user was not found', status=status.HTTP_404_NOT_FOUND)
    return response.Response(serializer.data, status=status.HTTP_200_OK)


class ActionListView(generics.ListAPIView):
    queryset = Actions.objects.all()
    serializer_class = ActionsListSerializer
