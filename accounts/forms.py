from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    """User login form"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

class RegistrationForm(UserCreationForm):
    """User registration form"""
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
    
    