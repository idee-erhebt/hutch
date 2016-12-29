from django import forms
from django.forms import PasswordInput,EmailInput
from .models import registered
class UserForm(forms.ModelForm):
    class Meta:
        model=registered
        fields=('emailid','password','password')
        widgets={
            'emailid': EmailInput(attrs={'required': True}),
            'password': PasswordInput(attrs={'required': True}),
        }

class tryform(forms.Form):
    eid=forms.CharField(widget=forms.EmailInput,max_length=20,required=True)
    password1 = forms.CharField(widget=forms.PasswordInput,required=True)
 #   named=forms.CharField(max_length=10)
