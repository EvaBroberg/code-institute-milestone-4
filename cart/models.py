from django.db import models
from products.models import Product

    
class Cart(models.Model):
    cart_id    = models.CharField(max_length=200, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']
        
    def __str__(self):
        return self.cart_id
        

class CartItem(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart     = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active   = models.BooleanField(default=True)
    
    class Meta:
        db_table = ''
        
    def sub_total(self):
        """
        calculate total amount based on quantity and price
        """
        return self.product.price*self.quantity
    
    def __str__(self):
        return self.product
