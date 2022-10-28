from django.shortcuts import render
from rest_framework  import viewsets
from Wallet.models import Customer, Wallet
from  .serializer import CustomerSerializer, WalletSerializer


# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    