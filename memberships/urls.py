from django.conf.urls import url, include
from . import views
from .views import PaymentView

urlpatterns = [
    url(r'^$', views.MembershipSelectView.as_view(template_name='membership_list.html'), name='select'),
    url(r'^payment/', PaymentView, name='payment'),
]
