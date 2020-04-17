from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=300, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    
    def get_absolute_url(self):
        return reverse("product_detail", kwargs={'pk':self.pk})
    
    
    def __str__(self):
        return self.name 