# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from accounts.forms import LoginForm, RegistrationForm, ContactForm
from django.contrib import messages
from django.forms import ModelForm
from .decorators import allowed_users
from .forms import CustomerForm
from django.http import HttpResponse

from memberships.models import *


def index(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        
        
        if contact_form.is_valid():
            contact_form.save()
            
            messages.success(request, 'form was posted')
                  
    else:
        contact_form = ContactForm()
    return render(request, 'index.html',{'contact_form':contact_form}) 


@login_required
def logout(request):
    """Logout user"""
    auth.logout(request)
    return redirect(reverse('index'))



def login(request):
    """Login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
            
            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, 'The Email Address or Password you entered is incorrect.')
    else:
        login_form = LoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def register(request):
    """Creates new user, assigns them to a a customer group and creates customer profile for that user"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            
            messages.success(request, 'Account for ' + username + ' was successfully created!')
            return redirect('login')
    
    context = {'form':form}
    
    return render(request, 'register.html', context) 



@login_required(login_url='login')
def userPage(request):
    """user account page"""
    return render(request, 'profile.html')


    


@login_required(login_url='login')
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        
        if form.is_valid():
            form.save()
    
    context = {'form':form}
    
    return render(request, 'profile.html', context)



def progress(request):
    return render(request, 'progress.html')
    








        
                
    