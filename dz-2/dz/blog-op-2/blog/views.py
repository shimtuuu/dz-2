
from django.shortcuts import render
from blog.models import Category, Post

def index(request):
    categories = Category.objects.all()  # Получаем все категории
    posts = Post.objects.all()  # Получаем все посты

    context = {
        'categories': categories,
        'posts': posts,
    }

    return render(
        request,
        'blog/index.html',
        context,
    )