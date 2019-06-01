from operator import itemgetter

from django.shortcuts import get_object_or_404, render
from .models import Item, CartItem, Cart

from django.http import HttpResponse, HttpResponseRedirect

from django.urls import reverse
from django.views import generic
from django.utils import timezone


def index(request):
    categories = Item.CATEGORIES
    items = Item.objects.all()
    cart = Cart.objects.first()
    context = {
        'categories': categories,
        'items': items,
        'cart': cart,

    }

    return render(request, 'clothes/index.html', context)


def item_detail(request, item_slug):
    item = Item.objects.get(slug=item_slug)
    cart = Cart.objects.first()
    context = {
        'item': item,
        'cart': cart,
    }

    return render(request, 'clothes/item.html', context)


def category(request, sex, category):
    items = Item.objects.all()
    cart = Cart.objects.first()

    if sex != 'any':
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
        'cart': cart,
    }

    return render(request, 'clothes/category.html', context)


def about(request):
    return render(request, 'clothes/about.html', {})


def test(request):
    return render(request, 'clothes/test11.html', {})


def cart_view(request):
    cart = Cart.objects.first()

    context = {
        'cart':cart
    }
    return render(request, 'clothes/cart.html', context)


def add_to_cart_view(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id=cart.id
        request.session['cart_id'] = cart.id
        cart = Cart.objects.get(id=cart_id)
        product = Item.objects.get(slug=product_slug)
        cart.add_to_cart(product.slug)
        return HttpResponseRedirect(reverse('cart'))


def remove_from_cart_view(request, product_slug):
    try:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
        request.session['total'] = cart.items.count()
    except:
        cart = Cart()
        cart.save()
        cart_id = cart.id
        request.session['cart_id'] = cart.id
        cart = Cart.objects.get(id=cart_id)
        product = Item.objects.get(slug=product_slug)
        cart.remove_from_cart(product.slug)
        return HttpResponseRedirect(reverse('cart'))
