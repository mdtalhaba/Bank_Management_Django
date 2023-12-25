from django.db import models
from accounts.models import UserBankAccount
from .constants import TRANSECTION_TYPE

class Transection(models.Model) :
    account = models.ForeignKey(UserBankAccount, related_name='transection', on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    balance_after_transection = models.DecimalField(decimal_places=2, max_digits=12)
    transection_type = models.IntegerField(choices=TRANSECTION_TYPE)
    timestamp = models.DateTimeField(auto_now_add=True)
    loan_approve = models.BooleanField(default=False)

    class Meta :
        ordering = ['timestamp']
