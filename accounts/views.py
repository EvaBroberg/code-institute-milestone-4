# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from accounts.forms import UserLoginForm


def index(request):
    """Return index page"""
    return render(request, 'index.html')

def logout(request):
    """Logout user"""
    auth.logout(request)
    return redirect(reverse('index'))

def login(request):
    """Return login page"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
            else:
                login_form.add_error(None, 'The Email Address or Password you entered is incorrect.')
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})