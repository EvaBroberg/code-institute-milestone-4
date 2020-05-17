from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.MembershipSelectView.as_view(template_name='membership_list.html'), name='select'),
]
