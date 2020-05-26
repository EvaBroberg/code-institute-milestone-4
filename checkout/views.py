from django.shortcuts import render, redirect
from cart.models import Cart, CartItem
from products.models import Product
from django.core.exceptions import ObjectDoesNotExist
from orders.models import Order, OrderItem
from cart.views import __cart_id

import stripe
from django.conf import settings



def checkout(request, total=0, counter=0, cart_items=None):
    """
    retrieve all cart items,
    calculate total cost of all products in the cart
    """
    try:
        cart       = Cart.objects.get(cart_id=__cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        
        for cart_item in cart_items:
            total   += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
            
    except ObjectDoesNotExist:
        pass

    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total   = int(total * 100) 
    description    = 'uGoGirl -New Order'
    data_key       = settings.STRIPE_PUBLISHABLE_KEY
    
    if request.method == 'POST':
        
        try:
            token           = request.POST['stripeToken']
            email           = request.POST['stripeEmail']
            
            billingName     = request.POST['stripeBillingName']
            billingAddress1 = request.POST['stripeBillingAddressLine1']
            billingCity     = request.POST['stripeBillingAddressCity']
            billingPostCode = request.POST['stripeBillingAddressZip']
            billingCountry  = request.POST['stripeBillingAddressCountryCode']
            
            shippingName     = request.POST['stripeShippingName']
            shippingAddress1 = request.POST['stripeShippingAddressLine1']
            shippingCity     = request.POST['stripeShippingAddressCity']
            shippingPostCode = request.POST['stripeShippingAddressZip']
            shippingCountry  = request.POST['stripeShippingAddressCountryCode']
            
            
            customer = stripe.Customer.create(
                email=email,
                source=token
                )
            
            charge = stripe.Charge.create(
                amount=stripe_total,
                currency='gbp',
                description=description,
                customer=customer.id
                )
            
            # create the order
            try:
                order_details = Order.objects.create(
                    token           = token,
                    total           = total,
                    email           = email,
                    
                    billingName     = billingName,
                    billingAddress1 = billingAddress1,
                    billingCity     = billingCity,
                    billingPostCode = billingPostCode,
                    billingCountry  = billingCountry,
                    
                    shippingName     = shippingName,
                    shippingAddress1 = shippingAddress1,
                    shippingCity     = shippingCity,
                    shippingPostCode = shippingPostCode,
                    shippingCountry  = shippingCountry
                    
                )
                
                order_details.save()
                
                for order_item in cart_items:
                    or_item = OrderItem.objects.create(
                        product  = order_item.product.name,
                        quantity = order_item.quantity,
                        price    = order_item.product.price,
                        order    = order_details 
                    )
                    
                    or_item.save()
                    
                    # reduce stock
                    products       = Product.objects.get(id=order_item.product.id)
                    products.stock = int(order_item.product.stock - order_item.quantity)
                    
                    products.save()
                    order_item.delete()
                
                return redirect('thank_you_page', order_details.id)
            
            except ObjectDoesNotExist:
                pass
                
            
            
        except stripe.error.CardError as e:
            return False, e
    
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter, data_key=data_key, stripe_total=stripe_total,description=description))