from django.db import models
from django.db.models import Avg

class Author(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True, default=None)
    biography =  models.CharField(max_length=1000)
    pic = models.ImageField(upload_to='uploads/', null=True)
    def __str__(self):
        return self.firstName +' '+self.lastName

class Book(models.Model):
    PURCHASE_CHOICES = [('New','New'),('Used','Used')]
    BOOK_TYPE = [('Hardback','Hardback'),('Paperback','Paperback')]
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='Author')
    publisher = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    condition = models.CharField(choices=PURCHASE_CHOICES, max_length=10, blank=True)
    type = models.CharField(choices=BOOK_TYPE, max_length=10)
    published_date=models.DateTimeField()
    cover = models.ImageField(upload_to='uploads/', null=True)
    cost = models.FloatField(null=True, blank=True, default=None)
    pages = models.IntegerField(null=True, blank=True, default=None)
    synopsis = models.CharField(max_length=1000, blank=True, null=True)
    ISBN = models.CharField(max_length=25, blank=True, null=True)
    dimensions = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.title

