from django import template
from django.db.models import Avg

from ratings.models import Review
from details.models import Book

register = template.Library()

@register.filter
def rating_avg(book):
    reviews = Review.objects.filter(book=book)
    return reviews.aggregate(Avg('rating'))['rating__avg']
