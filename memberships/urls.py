from django.urls import path
from django.conf.urls import url, include
from . import views
from .views import MembershipSelectView, PaymentView, updateTransactions

urlpatterns = [
    url(r'^$', views.MembershipSelectView.as_view(template_name='membership_list.html'), name='select'),
    url(r'^payment/', PaymentView, name='payment'),
    url(r'^update_transactions/(?P<stripe_subscription_id>[^/]+)', updateTransactions, name='update_transactions'),
]
