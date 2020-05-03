# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import LoginForm, RegistrationForm, ContactForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from .decorators import allowed_users


def index(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        
        if contact_form.is_valid():
            contact_form.save()
            
            # messages.success(request, 'form was posted')
                  
    else:
        contact_form = ContactForm()
    return render(request, 'index.html',{'contact_form':contact_form}) 


@login_required
def logout(request):
    """Logout user"""
    auth.logout(request)
    return redirect(reverse('index'))



def login(request):
    """Return login page"""
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
    """Return registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method == 'POST':
        registration_form = RegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],password=request.POST['password1'])
            
            if user:
                auth.login(user=user,request=request)
                return redirect(reverse('index'))
            else:
                #alert that unable to register
                pass
    else:
        registration_form = RegistrationForm()
    return render(request, 'register.html', {'registration_form': registration_form}) 




@login_required
@allowed_users(allowed_roles=['paying_member'])
def profile(request):
    """User profile page"""
    user = User.objects.get(email=request.user.email)
    
    if request.method == 'POST':
        user_update_form = UserUpdateForm(request.POST, instance=request.user)
        profile_update_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_update_form.is_valid() and profile_update_form.is_valid():
            user_update_form.save()
            profile_update_form.save()
            messages.success(request, f'Your profile had been updated!')
            return redirect('profile')
        
    else:
        user_update_form = UserUpdateForm(instance=request.user)
        profile_update_form = ProfileUpdateForm(instance=request.user.profile)
        
        
    return render(request, 'profile.html', {'profile':user, 'user_update_form':user_update_form, 'profile_update_form':profile_update_form})