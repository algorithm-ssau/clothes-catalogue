from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('item/(?<item_slug>[.\w]+)/s', views.item, name='item_detail'),
    path('item/<slug:item_slug>/', views.item_detail, name='item_detail'),
    path('category/<str:sex>/<str:category>/', views.category, name='category'),
    path('about', views.about, name='about'),
    path('test/', views.test, name='test'),
]
