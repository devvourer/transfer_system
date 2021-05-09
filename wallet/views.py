import decimal

from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework import generics, response, status
from rest_framework.renderers import JSONRenderer
from .serializer import TransferSerializer
from custom_auth.models import User
from .models import Wallet
from rest_framework import decorators
from .currency import get_currency
from currency_converter import CurrencyConverter

c = CurrencyConverter(decimal=True)


@decorators.api_view(['GET', 'POST'])
@decorators.renderer_classes([JSONRenderer,])
def transfer(request):
    serializer = TransferSerializer()
    # if request.method == 'POST':
    serializer = TransferSerializer(data=request.data)
    if serializer.is_valid():
        try:
            cd = serializer.data

            receiver = User.objects.get(email=cd['to_email'])
            receiver = Wallet.objects.get(user=receiver)
            sender = Wallet.objects.get(user=request.user)
            print(sender.balance)
            qwe = sender.balance - decimal.Decimal(cd['how_much'])
            sender.balance -= decimal.Decimal(cd['how_much'])
            if sender.balance < 0:
                raise Exception('balance cannot be less than zero')
            else:
                sender.save()
            if sender.currency == receiver.currency:
                receiver.balance += float(cd['how_much'])
                receiver.save()
                sender.save()
                return response.Response('IF WAS WORKING')
            else:
                summ = c.convert(float(cd['how_much']), sender.currency, receiver.currency)
                receiver.balance += summ
                receiver.save()
                sender.save()
                return response.Response('ELSE WORKED')
        except ObjectDoesNotExist:
            return response.Response('user was not found')

    return response.Response(serializer.data, status=status.HTTP_200_OK)

