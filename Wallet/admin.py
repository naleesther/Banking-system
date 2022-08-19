from ossaudiodev import SOUND_MIXER_SPEAKER
from django.contrib import admin

from Wallet.models import Customer
from .models import Account, Card, Customer, Loan, Notification, Receipt, Reward, ThirdParty, Transaction, Wallet


class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","address",)
    search_fields=("firstname","last_name",)
admin.site.register(Customer,CustomerAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display=("account_name","account_number","balance",)
    search_fields=("account_name","account_number",)
admin.site.register(Account,AccountAdmin) 

class WalletAdmin(admin.ModelAdmin):
    list_display=("customer","currency","balance",)
    search_fields=("Customer","Balance",)
admin.site.register(Wallet,WalletAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display=("wallet","amount","number",)
    search_fields=("wallet","number",)
admin.site.register(Transaction,TransactionAdmin)

class ThirdPartyAdmin(admin.ModelAdmin):
    list_display=("name","currency","account",)
    search_fields=("name","account",)
admin.site.register(ThirdParty,ThirdPartyAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display=("card_name","card_number","account",)
    search_fields=("card_name","account",)
admin.site.register(Card,CardAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display=("title","recipient","status",)
    search_fields=("title","recipient",)
admin.site.register(Notification,NotificationAdmin)


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'date', 'file')
    search_fields = ('date', 'transaction')
admin.site.register(Receipt, ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display=("wallet","balance","loan_amount",)
    search_fields=("wallet","balance",)
admin.site.register(Loan,LoanAdmin)
class RewardAdmin(admin.ModelAdmin):
    list_display = ("date", "wallet","points")
    search_fields =("wallet", "points")
admin.site.register(Reward, RewardAdmin)









# Register your models here.
