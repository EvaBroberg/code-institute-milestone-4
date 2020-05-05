# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _



class AccountsConfig(AppConfig):
    name = 'accounts'
    
    def ready(self):
        import accounts.signals