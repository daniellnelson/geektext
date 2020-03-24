from django.db import models
from django.db.models import Avg

class Author(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True, default=None)
    def __unicode__(self):
        return u'%s %s' % (self.firstname, self.lastname)

class Book(models.Model):
    PURCHASE_CHOICES = [('New','New'),('Used','Used')]
    BOOK_TYPE = [('Hardback','Hardback'),('Paperback','Paperback')]
    title = models.CharField(max_length=100)
    author = models.CharField(Author, max_length=200)
    publisher = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    condition = models.CharField(choices=PURCHASE_CHOICES, max_length=10, blank=True)
    type = models.CharField(choices=BOOK_TYPE, max_length=10)
    published_date=models.DateTimeField()
    cover = models.ImageField(upload_to='uploads/')
    cost = models.FloatField(null=True, blank=True, default=None)
    pages = models.IntegerField(null=True, blank=True, default=None)
    synopsis = models.CharField(max_length=1000, blank=True, null=True)
    ISBN = models.CharField(max_length=25, blank=True, null=True)
    dimensions = models.CharField(max_length=50, blank=True, null=True)
