from django.shortcuts import render

from  django.views.generic import ListView, DetailView

from .models import Plan
# Create your views here.

class PlanListView(ListView):
        model = Plan
        
class PlanDetailView(DetailView):
        model = Plan
    