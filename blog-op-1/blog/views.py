from django.shortcuts import render, get_object_or_404
from .models import Category, Post


def get_category(request, slug):
    # Получаем объект категории по slug или возвращаем 404, если не найден
    category = get_object_or_404(Category, slug=slug)[1]

    # Выбираем все посты, связанные с данной категорией
    posts = Post.objects.filter(category=category)[5]

    context = {
        'category': category,
        'posts': posts,
    }

    return render(request, 'category.html', context)[2]
