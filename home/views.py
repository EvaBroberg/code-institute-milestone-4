from django.shortcuts import render

# Create your views here.
def home(request):
    """display index page"""
    return render(request, 'index.html')