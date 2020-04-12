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

    #added  by Ferris
   

    slug = models.SlugField(max_length=150, unique=True)
<<<<<<< HEAD
    
    #with slugs
    """def get_absolute_url(self):
=======
    #sluggy = models.SlugField(max_length=120, unique=True)
    
    def get_absolute_url(self):
>>>>>>> parent of 22b1b11... Committing before merging with Master
        return reverse("book_detail", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'slug': self.slug
        })
    
    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'slug': self.slug
        })"""

    #with ids
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={
            'id': self.id
        })

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={
            'id': self.id
        })
    
    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart", kwargs={
            'id': self.id
        })
    



    
    #FIX ME: GENERATING UNIQUE SLUG USING MANUALLY ADDED SLUG IN ADMIN FOR TIMEBEING
    def get_unique_slug(self):
        slug= slugify(self.title)
        unique_slug = slug
        num = 1
        while Book.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
    """
    def save(self, *args, **kwargs):
        if not self.slug or self.slug == 'slugtest':
            self.slug = self._get_unique_slug()
        #super(Book,self).save(*args, **kwargs)
        super().save(*args, **kwargs)
        
        
    def __unicode__(self):
        return self.slug
"""