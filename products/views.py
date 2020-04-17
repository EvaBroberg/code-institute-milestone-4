from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def product_list_view(request):
    products = Product.objects.all()
    return render(request, "list.html", {"products": products})

def product_detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "detail.html", {"product": product})
