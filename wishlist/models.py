from django.db import models
from django.contrib.auth.models import User

from details.models import Book

class Wishlist(models.Model):
    listname = models.CharField(max_length=20, default='My Wishlist')
    created = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(Book, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
