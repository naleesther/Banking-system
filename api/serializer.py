
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from Wallet.models import Customer, Wallet

class CustomerSerializer(serializers.ModelSerializer):
     class Meta:
          model = Customer
          fields = ("first_name","email","age")

class WalletSerializer(serializers.ModelSerializer):
     class Meta:
          model = Wallet
          fields = ("customer","balance","currency")          