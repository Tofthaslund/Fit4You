from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name="blog"),
    path('blog/<int:pk>',
         views.ArticleDetailView.as_view(), name='blog_detail'),
    path('add',
         views.add_blog, name='add_blog'),
    path('edit/<int:blog_id>/',
         views.edit_blog, name='edit_blog'),
]
