from django.shortcuts import render
from products.models import Product


def search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "list.html", {"products":products})
