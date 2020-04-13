from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from rango.models import *
from rango.forms import *


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


def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database
            form.save(commit=True)
            return redirect('/rango/')
        else:
            # The supplied form has errors.
            print(form.errors)

    # Will handle the bad form, new form, or no form supplied cases
    return render(request, 'rango/add_category.html', {'form': form})


def add_page(request, category_name_slug):
    form = PageForm()
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        return redirect(f'/rango/')

    if request.method == 'POST':
        form = PageForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database
            page = form.save(commit=False)
            page.category = category
            page.save()
            return redirect(reverse('rango:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            # The supplied form has errors.
            print(form.errors)

    # Will handle the bad form, new form, or no form supplied cases
    return render(request, f'rango/add_page.html', {'category': category, 'form': form})
