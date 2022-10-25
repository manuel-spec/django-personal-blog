from django.urls import path
from .views import delete, homeView, BlogView, CreateBlogView, CreatePost, GetDetail,delSure
urlpatterns = [
    path('', homeView, name='home'),
    path('blogs', BlogView.as_view(), name='blog-index'),
    path('createBlog', CreateBlogView, name='create-blog'),
    path('post/', CreatePost, name='create-post'),
    path('blogs/<int:pk>', GetDetail, name='detail-view'),
    path('blogs/<int:pk>/del', delete, name='delete-view'),
    path('blogs/<int:pk>/deleted', delSure, name='delPostNow'),
]