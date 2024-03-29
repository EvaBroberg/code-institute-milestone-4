from django.db import models
from django.urls import reverse

        
# order

class Order(models.Model):
    token           = models.CharField(max_length=200, blank=True)
    total           = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='GBP Order Total')
    email           = models.EmailField(max_length=200, blank=True, verbose_name='Email Adress')
    created         = models.DateTimeField(auto_now_add=True)
    
    billingName     = models.CharField(max_length=200, blank=True)
    billingAddress1 = models.CharField(max_length=200, blank=True)
    billingCity     = models.CharField(max_length=200, blank=True)
    billingPostCode = models.CharField(max_length=200, blank=True)
    billingCountry  = models.CharField(max_length=200, blank=True)
    
    shippingName     = models.CharField(max_length=200, blank=True)
    shippingAddress1 = models.CharField(max_length=200, blank=True)
    shippingCity     = models.CharField(max_length=200, blank=True)
    shippingPostCode = models.CharField(max_length=200, blank=True)
    shippingCountry  = models.CharField(max_length=200, blank=True)
    
    class Meta:
        db_table = 'Order'
        ordering = ['-created']
        
    def __str__(self):
        return str(self.id)
    

class OrderItem(models.Model):
    product  = models.CharField(max_length=200)
    quantity = models.IntegerField() 
    price    = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='GBP Price')
    order    = models.ForeignKey(Order, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'OrderItem'
        
    def sub_total(self):
        """
        calculate subtotal of the total items
        """
        return self.quantity * self.price
    
    def __str__(self):
        return self.product
    
    
    
    
    
        
    
        
