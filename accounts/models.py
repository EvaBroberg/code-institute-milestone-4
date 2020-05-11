# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from products.models import Product

# Create your models here.

class Contact(models.Model):
    name    = models.CharField(max_length=100)
    email   = models.EmailField()
    message = models.TextField(max_length=2000)

class Customer(models.Model):
    """Creates user instance"""
    user         = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name         = models.CharField     (max_length=200, null=True)
    phone        = models.CharField     (max_length=200, null=True)
    email        = models.CharField     (max_length=200, null=True)
    profile_pic  = models.ImageField    (default='default.jpg', null=True, blank=True)
    date_created = models.DateTimeField (auto_now_add=True, null=True)
    
    
    def __str__(self):
        return self.name
            
        


