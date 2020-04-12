from django.contrib import admin

from .models import Book, Author



@admin.register(Book,Author)
class BookAdmin(admin.ModelAdmin):
    pass

"""
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover', 'author','genre', 'condition', 'type', 'cost', 'pages','slug']
    prepopulated_fields = {"slug": ("title",)}
"""
