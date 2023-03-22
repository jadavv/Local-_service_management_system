from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_servicer =models.BooleanField(default=False)
    is_customer =models.BooleanField(default=False,null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age= models.IntegerField(default=0)
   
    class Meta:
        db_table = 'User'
    
    
     
     
