from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index-page'),
    path('', views.StartingPageView.as_view(), name='index-page'),
    #path('posts', views.posts, name='posts-page'),
    path('posts', views.AllPostsView.as_view(), name='posts-page'),
    #path('posts/<slug:slug>', views.post_detail, name='post-detail-page'), # /posts/my-first-post
    path('posts/<slug:slug>', views.SinglePostView.as_view(), name='post-detail-page'), 
]