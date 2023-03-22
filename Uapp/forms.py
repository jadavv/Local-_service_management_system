from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User


class ServiceProviderRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields= ('first_name','last_name','username','email','password1','password2','age')
        
        @transaction.atomic
        def save(self):
            user= super().save(commit=False)
            user.is_servicer= True
            user.save()
            return user         
        
class CustomerRegisterForm(UserCreationForm):
    class Meta (UserCreationForm.Meta):
        model= User
        fields=('first_name','last_name','username','email','password1','password2','age')  
        
        @transaction.atomic
        def save(self):
            user=super().save(commit=False)
            user.is_customer= True
            user.save()
            return user
           
     


