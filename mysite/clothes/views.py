from django.shortcuts import get_object_or_404, render
from .models import Item

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone


def index(request):
    categories = Item.CATEGORIES
    items = Item.objects.all()
    context = {
        'categories': categories,
        'items': items,
    }

    return render(request, 'clothes/index.html', context)


def item_detail(request, item_slug):
    item = Item.objects.get(slug=item_slug)
    context = {
        'item': item
    }

    return render(request, 'clothes/item.html', context)


def category(request, sex, category):
    items = Item.objects.all()
    context = {
        'sex': sex,
        'category': category,
        'items': items,
    }

    return render(request, 'clothes/category.html', context)


def test(request):
    return render(request, 'clothes/test11.html', {})
