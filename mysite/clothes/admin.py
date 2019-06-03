from django.contrib import admin

from .models import Item
    # CartItem, Cart


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Item, ItemAdmin)
# admin.site.register(Cart)
# admin.site.register(CartItem)
