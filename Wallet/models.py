# from datetime import date
# from email import message
# from locale import currency
# from pyexpat import model
# from turtle import title
# from unicodedata import name
import code
from datetime import datetime
from inspect import signature
from locale import currency
from symtable import Symbol
# from tkinter import CASCADE
from django.db import models

class Customer (models.Model):
    first_name = models.CharField(max_length=15,null=True)
    last_name = models.CharField(max_length=15,null=True)
    address = models.TextField()
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10,null=True)
    age = models.PositiveSmallIntegerField()

class Account(models.Model):
    account_name=models.CharField(max_length=15,null=True)
    account_number=models.IntegerField()
    balance=models.IntegerField()
    account_type=models.CharField(max_length=15,null=True)

class Wallet(models.Model):
    balance=models.IntegerField()
    pin=models.IntegerField()
    status=models.CharField(max_length=15,null=True)
    customer=models.ForeignKey(Customer,default=1,on_delete=models.CASCADE)
    date_created=models.DateTimeField(null=True)
    currency=models.CharField(max_length=15,null=True)   

class Transaction(models.Model):
    date=models.DateTimeField()
    amount=models.IntegerField()
    number=models.IntegerField()
    code=models.CharField(max_length=10,null=True)
    wallet=models.ForeignKey(to=Wallet,on_delete=models.CASCADE)
    transaction_type=models.CharField(max_length=15)
    receipt=models.ForeignKey(to=Customer,on_delete=models.CASCADE)
    transaction_charge=models.IntegerField()
    origin_account=models.ForeignKey(to=Account,on_delete=models.CASCADE, related_name="origin_transaction", null=True)
    destination_account=models.ForeignKey(to=Account,on_delete=models.CASCADE, related_name="destination_transaction", null=True)
    
class ThirdParty(models.Model):
    name=models.CharField(max_length=15,null=True)
    currency=models.IntegerField()
    transaction_cost=models.IntegerField(default=1)
    account=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)


class Card(models.Model):
    card_name=models.CharField(max_length=15,null=True)
    card_number=models.IntegerField()
    card_type=models.CharField(max_length=10,null=True)
    expiry_date=models.DateTimeField(default=datetime.now)
    security_code=models.IntegerField()
    account=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)
    issuer=models.CharField(max_length=15,null=True)

class Notification(models.Model):
    title=models.CharField(max_length=15,null=True)
    message=models.CharField(max_length=15,null=True)
    date=models.DateTimeField()
    recipient=models.ForeignKey(to=Customer,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=6,null=True)


class Receipt(models.Model):
    receipt_type = models.CharField(null=True, max_length=10)
    date = models.DateTimeField(null=True)
    transaction = models.ForeignKey(null=True, to=Transaction, on_delete=models.CASCADE, related_name='receipt_transaction')
    file = models.FileField(null=True)

class Loan(models.Model):
    loan_amount=models.IntegerField(null=True)
    loan_intrest=models.IntegerField(null=True)
    due_date=models.DateTimeField(default=datetime.now)
    loan_ID=models.IntegerField(null=True)
    purpose=models.CharField(max_length=15,null=True)
    loan_status=models.CharField(max_length=15,null=True)
    date_issued=models.DateTimeField(default=datetime.now)
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,null=True)
    balance=models.IntegerField(null=True)
    guarantor=models.ForeignKey(Account,on_delete=models.CASCADE,null=True)


class Reward(models.Model):
    reward_reciepient=models.CharField(max_length=15,null=True)
    date=models.DateTimeField()
    wallet=models.ForeignKey(Wallet,on_delete=models.CASCADE,null=True)
    points=models.IntegerField(null=True)

class Currency(models.Model):
    country_origin=models.CharField(max_length=10,null=True)
    Symbol=models.CharField(max_length=10,null=True)
    amount=models.BigIntegerField()    


    