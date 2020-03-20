from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$',views.PostListView.as_view(),name='post_list'),
    url(r'post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name='post_detail'),
    url(r'post/new/$',views.CreatePostView.as_view(),name='post_new'),
]