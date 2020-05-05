
from django.conf.urls import url, include
from .views import product_list_view, product_detail_view

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', product_detail_view, name='product_detail'),
    url(r'^$', product_list_view, name='products')  
]
