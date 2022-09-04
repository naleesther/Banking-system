from unicodedata import name
from django.urls import path
from .views import register_account, register_card, register_currency, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdParty, register_transaction, register_wallet

urlpatterns =[
    path("register/",register_customer,name="registration"),
    path("account/",register_account,name="account"),
    path("wallet/",register_wallet,name="wallet"),
    path("transaction/",register_transaction,name="transaction"),
    path("thirdParty/",register_thirdParty,name="thirdParty"),
    path("card/",register_card,name="card"),
    path("notification/",register_notification,name="notification"),
    path("receipt/",register_receipt,name="receipt"),
    path("loan/",register_loan,name="loan"),
    path("reward/",register_reward,name="reward"),
    path("currency/",register_currency,name="currency"),






]