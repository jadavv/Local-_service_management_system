from django import forms
from .models import LSadmin
from user.models import User

class LSadmin(forms.ModelForm):
    class Meta:
        model =LSadmin
        fields ='__all__'