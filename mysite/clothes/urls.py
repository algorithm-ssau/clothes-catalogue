from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('item/(?<item_slug>[.\w]+)/s', views.item, name='item_detail'),
    path('item/<slug:item_slug>/', views.item_detail, name='item_detail'),
    path('category/<str:sex>/<str:category>/', views.category, name='category'),
    path('about', views.about, name='about'),
    path('test/', views.test, name='test'),
    path('cart/', views.cart_view, name='cart'),
    path('item/<slug:item_slug>/add_to_cart/<slug:product_slug>/', views.add_to_cart_view, name='add_to_cart'),
path('item/<slug:item_slug>/add_to_cart/', views.add_to_cart_view, name='add_to_cart'),
    path('cart/', views.remove_from_cart_view, name='remove_from_cart'),

]
