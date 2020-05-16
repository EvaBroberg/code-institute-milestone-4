from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.PlanListView.as_view(template_name='plan_list.html'), name='plan_list'),
    url(r'^plan/(?P<pk>\d+)$',views.PlanDetailView.as_view(template_name='plan_detail.html'),name='plan_detail'),
]




