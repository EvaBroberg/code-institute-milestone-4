from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import *

class CustomerForm(ModelForm):
    """
    customers are able to update their own information
    but they are not able to update the user
    """
    class Meta:
        model   = Customer
        fields  = '__all__'
        exclude = ['user']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
                

class LoginForm(forms.Form):
    """User login form"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class RegistrationForm(UserCreationForm):
    """User registration form"""
    class Meta:
        model  = User
        fields = ['username', 'email', 'password1', 'password2']

        

def clean_email(self):
    email = self.cleaned_data.get('email')
    username = self.cleaned_data.get('username')
    if User.objects.filter(email=email).exclude(username=username):
        raise forms.ValidationError(u'This email is already registered.')
    return email



def clean_password(self):
    password1 = self.cleaned_data.get('password1')
    password2 = self.cleaned_data.get('password2')
    if not password1 or not password2:
        raise forms.ValidationError(u'Please confirm your password.')
    if password1 != password2:
        raise forms.ValidationError(u'Passwords must match.')
    return password2


    
