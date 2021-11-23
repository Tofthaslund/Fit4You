from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view(), name="blog"),
    path('blog/<int:pk>',
         views.ArticleDetailView.as_view(), name='blog_detail'),
]
