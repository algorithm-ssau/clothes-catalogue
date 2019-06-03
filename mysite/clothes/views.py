from operator import itemgetter

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
        'item': item,
    }
    return render(request, 'clothes/item.html', context)


def category(request, sex, category):
    items = Item.objects.all()

    if sex != 'anygender':
        if sex == 'women':
            items = items.filter(gender__in=['women', 'unisex'])
        if sex == 'men':
            items = items.filter(gender__in=['men', 'unisex'])
        if sex == 'kids':
            items = items.filter(gender__in=['kids'])

    if category != 'all':
        if category in map(itemgetter(0), Item.CATEGORIES):
            items = items.filter(category=category)
        else:
            if category == 'tops':
                items = items.filter(category__in=['shirts', 'coats', 'sweatshirts', 'blouses', 'pullovers', 'tshirts'])
            if category == 'bottoms':
                items = items.filter(category__in=['trousers', 'shorts', 'skirts'])

    context = {
        'gender': sex,
        'category': category,
        'items': items,
    }

    return render(request, 'clothes/category.html', context)

def about(request):
    return render(request, 'clothes/about.html', {})