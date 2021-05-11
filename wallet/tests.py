import decimal
from django.test import TestCase
from rest_framework import status

from .models import Wallet
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory
from .views import transfer, ActionListView
from actions.models import Actions

User = get_user_model()


class WalletTestCases(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='testuser@mail.com', password='password')
        user2 = User.objects.create(email='testuser2@mail.com', password='password')
        wallet = Wallet.objects.create(user=self.user, balance=decimal.Decimal(100))
        wallet2= Wallet.objects.create(user=user2, currency='USD', balance=decimal.Decimal(100))
        self.user.save()
        self.client.login(email='testuser@mail.com', password='password')

    def test_transfer(self):
        wallet = Wallet.objects.first()
        factory = APIRequestFactory()
        request = factory.get('')
        request.user = self.user
        response = transfer(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_action_list(self):
        factory = APIRequestFactory()
        request = factory.get('')
        request.user = self.user
        response = ActionListView.as_view()(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

