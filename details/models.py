from django.db import models
from django.shortcuts import reverse
from django.conf import settings
from django.utils.text import slugify
from django_extensions.db.fields import AutoSlugField



#for random slug generating
import random
import string
import itertools



class Author(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True, default=None)
    def __unicode__(self):
        return u'%s %s' % (self.firstName, self.lastName)

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

    #added  by Ferris
    
    #slug = models.SlugField(max_length=200)
    slug = models.SlugField(max_length = 150)
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={
            'slug': self.slug
        })
    
    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })

    
  