from django.db import models
from custom_auth.models import User


USD = 'USD'
EUR = 'EUR'
BTC = 'BTC'
GBP = 'GBP'
RUB = 'RUB'

CURRENCY_CHOICES = (
    (USD, 'Us dollars'),
    (EUR, 'Euro'),
    (GBP, 'Uk pounds'),
    (BTC, 'Bitcoin'),
    (RUB, 'Rubles')
)


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.CharField(choices=CURRENCY_CHOICES, default=EUR, max_length=3)
    balance = models.DecimalField(max_digits=9, decimal_places=2, default=10)

