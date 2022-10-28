from unicodedata import name
# from click import edit
from django.urls import path
from .views import account_profile, card_profile, customer_profile, edit_profile, list_account,list_cards, list_currencys,list_customers,list_loans,list_notifications, list_receipts, list_rewards,list_thirdPartys,list_transactions,list_wallet, register_account, register_card, register_currency, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdParty, register_transaction, register_wallet, transaction_profile, wallet_profile

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
    path("customers/",list_customers,name="customers_list"),
    path("accounts/",list_account,name="account_list"),
    path("wallets/",list_wallet, name="wallet_list"),
    path("transactions/",list_transactions, name="transactions_list"),
    path("thirdPartys/",list_thirdPartys, name="thirdPartys_list"),
    path("cards/",list_cards,name="list_cards"),
    path("notifications/",list_notifications,name="notifications_list"),
    path("receipts/",list_receipts,name="receipts_list"),
    path("loans/",list_loans,name="loans_list"),
    path("rewards/",list_rewards,name="rewards_list"),
    path("currencys/",list_currencys,name="currencys_list"),

    path("customerss/<int:id>/", customer_profile,name="customer_profile"),
    path("customerss/edit/<int:id>/",edit_profile,name="edit_profile"),
    path("wallets/<int:id>",wallet_profile,name="wallet_profile"),
    path("wallets/edit/<int:id>/",edit_profile,name="edit_wallet"),
    path("accountss/<int:id>/",account_profile,name="account_profile"),
    path("accountss/edit/<int:id>/",edit_profile,name="edit_profile"),
    path("cards/<int:id>/",card_profile,name="card_profile"),
    path("cards/edit/<int:id>/",edit_profile,name="edit_profile"),
    path("transactions/<int:id>/",transaction_profile,name="transaction_profile"),
    path("transactions/edit/<int:id>/",edit_profile,name="edit_profile"),





    

]