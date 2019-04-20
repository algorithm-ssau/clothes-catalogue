from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone


def index(request):
    return render(request, 'clothes/index.html')


def hello_world(request):
    return render(request, 'base.html', {})

