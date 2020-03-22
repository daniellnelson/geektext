from django.contrib import admin
from .models import Wishlist

@admin.register(Wishlist)
class WishAdmin(admin.ModelAdmin):
    list_display = ['listname', 'created']
