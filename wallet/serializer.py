from rest_framework import serializers
from .models import Wallet


class WalletCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('currency', 'balance')


class TransferSerializer(serializers.ModelSerializer):
    to_email = serializers.EmailField()
    how_much = serializers.DecimalField(max_digits=9, decimal_places=2)

    class Meta:
        model = Wallet
        fields = ('to_email', 'how_much')
