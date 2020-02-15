from django.db import models

from details.models import Book

class Wishlist(models.Model):
    listname = models.CharField(max_length=20, default='My Wishlist')
    created = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(Book, blank=True)
