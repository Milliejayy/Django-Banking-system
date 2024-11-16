from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class UserForm(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, unique=True)
    password = models.CharField(max_length=25)
    balance = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self):
        if not self.account_number :
            self.account_number = str(uuid.uuid4().int)[:15]
            return super().save()
        

    def __str__(self):
        return f'{self.balance} \n {self.account_number}'
    
