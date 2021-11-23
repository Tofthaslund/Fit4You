from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Blog

from .forms import BlogForm


class ArticleListView(ListView):
    model = Blog
    template_name = "blog/blog.html"


class ArticleDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'