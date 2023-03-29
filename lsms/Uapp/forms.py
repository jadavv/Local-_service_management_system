from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User


class ServiceProviderRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields= ('first_name','last_name','username','email','password1','password2','age','is_servicer')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter Password'}),
            'age':forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
            # 'is_servicer':forms.BooleanField(attrs={'class':'form-control','placeholder':'is_servicer'}),
        }
        
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
        
        widgets ={
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter Password'}),
            'age':forms.TextInput(attrs={'class':'form-control','placeholder':'Age'}),
            
            
        }
        
        @transaction.atomic
        def save(self):
            user=super().save(commit=False)
            user.is_customer= True
            user.save()
            return user

class AdminRegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email','password1','password2')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        return user  
           
     


