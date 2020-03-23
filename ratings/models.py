from django.db import models
from django.contrib.auth import get_user_model
from details.models import Book
# Create your models here.

class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    rating = models.DecimalField(decimal_places=1, max_digits=2, default=0)

    class Meta:
        ordering = ['-rating']

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50, null=True, default='anonymous user')
    body = models.TextField()
    #created_on = models.DateTimeField()
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
