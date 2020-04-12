from django.contrib import admin

from .models import Book, Author


@admin.register(Book,Author)
class BookAdmin(admin.ModelAdmin):
    pass
