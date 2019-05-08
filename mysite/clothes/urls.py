from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('item/(?<item_slug>[.\w]+)/s', views.item, name='item_detail'),
    path('item/<slug:item_slug>/', views.item, name='item_detail'),
]
