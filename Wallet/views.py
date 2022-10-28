from django.shortcuts import redirect, render

from Wallet.models import Account,Card, Currency, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet
from .forms import AccountRegistrationForm, CardRegistrationForm, CurrencyRegistrationForm, CustomerRegistrationForm, LoanRegistrationForm, NotificationRegistrationForm, ReceiptRegistrationForm, RewardRegistrationForm, ThirdPartyRegistrationForm, TransactionRegistrationForm, WalletRegistrationForm

# Create your views here.
#handles Http request for registering the customer.

def register_customer(request):
    if request.method == "POST":
       form=CustomerRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
       form = CustomerRegistrationForm()
    return render(request,"wallet/register_customer.html",{"form":form})

def list_customers(request):
    customer=Customer.objects.all()
    return render(request,"wallet/customerList.html",{"customer":customer})




def register_account(request):
    if request.method=="POST":
        form=AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=AccountRegistrationForm()
        return render(request,"wallet/account.html",{"form":form})

def list_account(request):
    accounts=Account.objects.all()
    return render(request,"wallet/accountList.html",{"accounts":accounts})




def register_wallet(request):
    if request.method=="POST":
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form=WalletRegistrationForm()
        return render(request,"wallet.html",{"form":form})

def list_wallet(request):
    wallets=Wallet.objects.all()
    return render(request,"wallet/wallet_list.html",{"wallets":wallets})




def register_transaction(request):
    if request.method=="POST":
       form=TransactionRegistrationForm(request.POST)
       if form.is_valid():
           form.save()
    else:
        form=TransactionRegistrationForm()
        return render(request,"transaction.html",{"form":form})

def list_transactions(request):
    transaction=Transaction.objects.all()
    return render (request,"transactions_list.html",{"transaction":transaction})               




def register_thirdParty(request):
    if request.method=="POST":
       form=ThirdPartyRegistrationForm(request.POST)
       if form.is_valid():
          form.save()
    else:
        form=ThirdPartyRegistrationForm()
        return render(request,"thirdParty.html",{"form":form})

def list_thirdPartys(request):
    thirdPartys=ThirdParty.objects.all()
    return render (request,"thirdPartys_list.html",{"thirdPartys":thirdPartys})        




def register_card(request):
    if request.method=="POST":
       form=CardRegistrationForm(request.POST)
       if form.is_valid():
        form.save()

    else:
        form=CardRegistrationForm()
        return render (request,"card.html",{"form":form})

def list_cards(request):
    cards=Card.objects.all()
    return render (request,"wallet/cards_list.html",{"cards":cards})  




def register_notification(request):
    if request.method=="POST":
       form=NotificationRegistrationForm(request.POST)
       if form.is_valid():
        form.save()
    else:
        form=NotificationRegistrationForm()
        return render (request,"notification.html",{"form":form}) 
def list_notifications(request):
    notifications=Notification.objects.all()
    return render (request,"notifications_list.html",{"notifications":notifications})




def register_receipt(request):
    if request.method=="POST":
        form=ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=ReceiptRegistrationForm()
        return render (request,"receipt.html",{"form":form})  
def list_receipts(request):
    receipts=Receipt.objects.all()
    return render (request,"receipts_list.html",{"receipts":receipts})   



   
def register_loan(request):
    if request.method=="POST":
      form=LoanRegistrationForm(request.POST)
      if form.is_valid():
         form.save()
    else:
        form=LoanRegistrationForm()     
        return render(request,"loan.html",{"form":form})
def list_loans(request):
    loans=Loan.objects.all()
    return render (request,"loans_list.html",{"loans":loans})  





def register_reward(request):
    if request.method=="POST":
     form=RewardRegistrationForm(request.POST)
     if form.is_valid():
        form.save()
    else:
        form=RewardRegistrationForm()    
        return render(request,"reward.html",{"form":form})
def list_rewards(request):
    rewards=Reward.objects.all()
    return render (request,"rewards_list.html",{"rewards":rewards})  


def register_currency(request):
    if request.method=="POST":      
       form=CurrencyRegistrationForm(request.POST)
       if form.is_valid():
           form.save()
    else:
        form=CurrencyRegistrationForm()       
        return render(request,"currency.html",{"form":form})
def list_currencys(request):
    currencys=Currency.objects.all()
    return render (request,"currencys_list.html",{"currencys":currencys})  


def customer_profile(request,id):
    customer = Customer.objects.get(id=id)
    return render (request, "wallet/customer_profile.html",{"customer":customer})   

def edit_profile(request,id):
    customer = Customer.objects.get(id=id)
    if request.method == "POST":
        form= (CustomerRegistrationForm(request.POST,instance=Customer))
        if form.is_valid():
            form.save()
        return redirect("customerss_profile",id=customer.id)
    else:
        form=CustomerRegistrationForm(instance=customer)
        return render(request,"wallet/edit_profile.html",{"form":form})              


def wallet_profile(request,id):
    wallet = Wallet.objects.get(id=id)
    return render (request, "wallet/wallet_profile.html",{"wallet":wallet})   

def edit_profile(request,id):
    wallet = Wallet.objects.get(id=id)
    if request.method == "POST":
        form= (WalletRegistrationForm(request.POST,instance=Wallet))
        if form.is_valid():
            form.save()
        return redirect("wallets_profile",id=wallet.id)
    else:
        form=WalletRegistrationForm(instance=wallet)
        return render(request,"wallet/edit_profile.html",{"form":form}) 
        

def account_profile(request,id):
     account = Account.objects.get(id=id)
     return render (request, "wallet/account_profile.html",{"account":account})   

def edit_profile(request,id):
    account = Account.objects.get(id=id)
    if request.method == "POST":
        form= AccountRegistrationForm(request.POST,instance=account)
        if form.is_valid():
            form.save()
        return redirect("account_profile",id=account.id)
    else:
        form=AccountRegistrationForm(instance=account)
        return render(request,"wallet/edit_profile.html",{"form":form}) 



def card_profile(request,id):
    card=Card.objects.get(id=id)
    return render (request, "wallet/card_profile.html",{"card":card})   

def edit_profile(request,id):
    card = Card.objects.get(id=id)
    if request.method == "POST":
        form= CardRegistrationForm(request.POST,instance=card)
        if form.is_valid():
            form.save()
        return redirect("card_profile",id=Card.id)
    else:
        form=CardRegistrationForm(instance=card)
        return render(request,"wallet/edit_profile.html",{"form":form}) 


def transaction_profile(request,id):
    transaction=Transaction.objects.get(id=id)
    return render (request, "wallet/transaction_profile.html",{"transaction":transaction})   

def edit_profile(request,id):
    transaction = Transaction.objects.get(id=id)
    if request.method == "POST":
        form= TransactionRegistrationForm(request.POST,instance=transaction)
        if form.is_valid():
            form.save()
        return redirect("transaction_profile",id=Transaction.id)
    else:
        form=TransactionRegistrationForm(instance=transaction)
        return render(request,"wallet/edit_profile.html",{"form":form}) 




