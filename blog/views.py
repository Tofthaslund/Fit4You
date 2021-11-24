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


@login_required
def add_blog(request):
    # Add an blog article to the blog. Only for superusers
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Store owner can do thay')
        return redirect(reverse('blog'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added new content to Blog')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to add New Blog. Please ensure form is valid')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form
    }

    return render(request, template, context)


@login_required
def edit_blog(request, blog_id):
    # Edit a blog. Only for superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Store owner can do thay')
        return redirect(reverse('blog'))

    blog = get_object_or_404(Blog, pk=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog Has Been Updates')
            return redirect(reverse('blog_detail', args=[blog.id]))
        else:
            messages.error(request, 'Failed to update Blog, please ensure form is valid')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog
    }

    return render(request, template, context)
