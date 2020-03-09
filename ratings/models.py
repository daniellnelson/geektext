from django.db import models
from django.contrib.auth.models import User
from details.models import Book
from geekprofile.models import Profile
from django.utils.timezone import now
# Create your models here.

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    anonymous = models.BooleanField()
    rating = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    comment = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ['user']

    def __str__(self):
        return 'Comment by {} -- {}'.format(self.user, self.book.title)
