from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class User_Info(models.Model):
    first_name = models.CharField(max_length=150, default="No")
    middle_name = models.CharField(max_length=150, default="No")
    last_name = models.CharField(max_length=150, default="No")
    id_number = models.IntegerField(default=0)
    email_address = models.EmailField(default="No")
    phone_number = models.IntegerField(default=0)