from django.db.models import Q
from django.shortcuts import render
from products.models import Product


def search(request):
    # products = Product.objects.filter(name__icontains=request.GET['q'])
    products = Product.objects.filter (
        Q(name__icontains=request.GET['q']) |
        Q(description__icontains=request.GET['q']) |
        Q(tag__title__icontains=request.GET['q'])
    )
    return render(request, "list.html", {"products":products})


    


