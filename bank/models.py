from django.contrib.auth.models import User
from django.db import models
import uuid

# Create your models here.


class BankAccount(models.Model):
    user = models.ForeignKey(User,models.CASCADE)
    bank_account = models.UUIDField(default=uuid.uuid4)
    balance = models.FloatField(default=0)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}"