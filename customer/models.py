from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomerUser(AbstractUser):
    sex_choise = ((0,'Nữ'),(1,'Nam'))
    sex = models.IntegerField(default=0,choices=sex_choise)
    address = models.CharField(default='',max_length=250)
    phone = models.CharField(default='',max_length=15)