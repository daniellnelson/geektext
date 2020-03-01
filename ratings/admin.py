from django.contrib import admin
from .models import Rating, Comment
# Register your models here.

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['book', 'rating']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'book', 'active')
    #list_filter = ('active')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, reuest, queryset):
        queryset.update(active=True)
# Register your models here.
