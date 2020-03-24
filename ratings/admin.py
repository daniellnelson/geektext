from django.contrib import admin
from .models import Review
# Register your models here.

# admin.site.register(Review)
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'rating', 'comment']
