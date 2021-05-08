from rest_framework import serializers
from .models import Wallet


class WalletCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('currency', 'balance')