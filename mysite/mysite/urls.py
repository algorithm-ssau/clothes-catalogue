from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('clothes/', include('clothes.urls')),
    path('admin/', admin.site.urls),
    path('', include('clothes.urls')),
]
