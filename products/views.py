from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def shop(request, category_slug = None):
    category = None 
    products = None
    
    if category_slug!=None:
        category = get_object_or_404(Category,slug=category_slug)
        products = Product.objects.filter(category=category, available=True)
    else:
        products = Product.objects.all().filter(available=True)
    
    return render(request, 'shop.html', {'category':category, 'products':products})

def productPage(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e 
    
    return render(request, 'product.html', {'product':product})