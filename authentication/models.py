from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserToken(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) #User
    token = models.UUIDField() # generated token for a user 