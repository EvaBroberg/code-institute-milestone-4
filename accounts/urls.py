from django.conf.urls import url, include
from accounts.views import *
from django.contrib.auth import views
from accounts import url_reset

urlpatterns = [
    # url(r'index',index, name='index'), 
    url(r'^logout/$',logout, name='logout'),
    url(r'^login/$',login, name='login'),
    url(r'^register/$',register, name='register'),
    # url(r'^profile/$',profile, name='profile'),
    url(r'^password-reset/', include(url_reset)),
    # url(r'^user/$', userPage, name='user-page'),
    url(r'^user/$', accountSettings, name='user-page'),
    url(r'^user/progress/$', progress, name='progress')
]
