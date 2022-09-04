from django.shortcuts import render

from Wallet.models import Customer
from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

# Create your views here.
#handles Http request for registering the customer.

def register_customer(request):
    form=CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form})


def register_account(request):
    form=AccountRegistrationForm()
    return render(request,"account.html",{"form":form})


def register_wallet(request):
    form=WalletRegistrationForm()
    return render(request,"wallet.html",{"form":form})

def register_transaction(request):
    form=TransactionRegistrationForm()
    return render(request,"transaction.html",{"form":form})

def register_thirdParty(request):
    form=ThirdPartyRegistrationForm()
    return render(request,"thirdParty.html",{"form":form})

def register_card(request):
    form=CardRegistrationForm()
    return render(request,"card.html",{"form":form})

def register_notification(request):
    form=NotificationRegistrationForm()
    return render(request,"notification.html",{"form":form})

def register_receipt(request):
    form=ReceiptRegistrationForm()
    return render(request,"receipt.html",{"form":form})

def register_loan(request):
    form=LoanRegistrationForm()
    return render(request,"loan.html",{"form":form})

def register_reward(request):
    form=RewardRegistrationForm()
    return render(request,"reward.html",{"form":form})

def register_currency(request):
    form=CurrencyRegistrationForm()
    return render(request,"currency.html",{"form":form})


