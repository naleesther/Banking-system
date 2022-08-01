from django.contrib import admin

from Wallet.models import Customer
from .models import Account, Card, Customer, Loan, Notification, Reciept, Reward, ThirdParty, Transaction, Wallet


class CustomerAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","address",)
    search_fields=("firstname","last_name",)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(Account) 
admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(ThirdParty)
admin.site.register(Card)
admin.site.register(Notification)
admin.site.register(Reciept)
admin.site.register(Loan)
admin.site.register(Reward)









# Register your models here.
