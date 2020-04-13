from django.http import HttpResponse
from django.shortcuts import render
from rango.models import *


def index(request):
    # top 5 categories (in likes)
    most_liked_categories = Category.objects.order_by('-likes')[:5]
    most_viewed_pages = Page.objects.order_by('-views')[:5]
    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
        'categories': most_liked_categories,
        'pages': most_viewed_pages,
    }
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    return render(request, 'rango/about.html')


def show_category(request, category_name_slug):
    try:
        # can we find a category name with the given slug?
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict = {'pages': pages, 'category': category}
    except Category.DoesNotExist:
        context_dict = {'category': None, 'pages': None}

    return render(request, 'rango/category.html', context=context_dict)