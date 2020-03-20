from django.db import models
from products.models import Product

# Create your models here.

class Order(models.Model):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False, default='')
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=True)
    postcode = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=40, blank=False)
    address1 = models.CharField(max_length=50, blank=False)
    address2 = models.CharField(max_length=50, blank=True)
    date = models.DateField()
    
    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.first_name, self.last_name )
    
    
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, null=False, on_delete = models.CASCADE)
    quantity = models.IntegerField(blank=False)
    
    def __str__(self):
        return "{0} {1} @ {2}".format(self.quantity, self.product.name, self.product.price)