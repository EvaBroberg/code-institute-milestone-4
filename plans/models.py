from django.db import models
from django.urls import reverse

from memberships.models import Membership

class Plan(models.Model):
    title               = models.CharField(max_length=200)
    description         = models.TextField(max_length=500)
    #change to foreign key field
    allowed_memberships = models.ManyToManyField(Membership)

    def __str__(self):
        return self.title
   
    def get_absolute_url(self):
       return reverse('plan_detail', kwargs={'pk': self.pk})
    
class PagesAccess(models.Model):
    title    = models.CharField(max_length=200)
    page     = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    position = models.IntegerField() 
    
    def __str__(self):
        return self.title