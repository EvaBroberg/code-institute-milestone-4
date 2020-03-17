from django.conf.urls import urls
from views import checkout

urlpatterns = [
    url(r'^$', checkout, name='checkout'),
]