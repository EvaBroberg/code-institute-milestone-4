from django.shortcuts import render

# Create your views here.
def index(request):
    """display index page"""
    return render(request, 'index.html')