from django.conf.urls import url
from .views import view_cart, add_to_cart, adjust_cart

urlpatterns = [
    url('^$', view_cart, name='view_cart'),
    url('^add/(?P<id>\d+)', add_to_cart, name='add_to_cart'),
    url('^adjust/(?P<id>\d+)',adjust_cart, name='adjust_cart'),
]