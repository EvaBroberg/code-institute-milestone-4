from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from orders.models import Order, OrderItem
from django.contrib import messages

import stripe
from django.conf import settings


def __cart_id(request):
    cart = request.session.session_key
    
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    """
    Add product to the cart and update it's quantity
    """
    product = Product.objects.get(id=product_id)
    
    try:
        cart = Cart.objects.get(cart_id=__cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=__cart_id(request))
        cart.save()
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1,cart=cart)
        cart_item.save()
         
    return redirect('add_cart')

    
    
def cart_remove(request, product_id):
    cart      = Cart.objects.get(cart_id=__cart_id(request))
    product   = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('add_cart')


def cart_delete(request, product_id):
    cart      = Cart.objects.get(cart_id=__cart_id(request))
    product   = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    
    return redirect('add_cart')



def thank_you_page(request, order_id):
    if order_id:
        customer_order = get_object_or_404(Order, id=order_id)
    return render(request, 'thankyou.html', {'customer_order': customer_order})








