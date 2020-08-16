from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(template_name='post_list.html'), name='post_list'),
    path('post/<int:pk>/',views.PostDetailView.as_view(template_name='post_detail.html'),name='post_detail'),
    path('post/new/',views.CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>/edit/',views.PostUpdateView.as_view(template_name='post_form.html'),name='post_edit'),
    path('post/<int:pk>/remove/',views.PostDeleteView.as_view(template_name='post_confirm_delete.html'),name='post_remove'),
    path('drafts/',views.DraftListView.as_view(),name='post_draft_list'),
    path('post/<int:pk>/comment/',views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/',views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/',views.comment_remove, name='comment_remove'),
    path('comment/<int:pk>/publish/',views.post_publish, name='post_publish'),
]