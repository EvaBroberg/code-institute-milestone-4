from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.PostListView.as_view(template_name='post_list.html'), name='post_list'),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(template_name='post_detail.html'),name='post_detail'),
    url(r'^post/new/$',views.CreatePostView.as_view(),name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$',views.PostUpdateView.as_view(template_name='post_form.html'),name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$',views.PostDeleteView.as_view(template_name='post_confirm_delete.html'),name='post_remove'),
    url(r'^drafts/$',views.DraftListView.as_view(),name='post_draft_list'),
    url(r'^post/(?P<pk>\d+)/comment/$',views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$',views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$',views.comment_remove, name='comment_remove'),
    url(r'^comment/(?P<pk>\d+)/publish/$',views.post_publish, name='post_publish'),
]

