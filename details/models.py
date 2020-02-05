from django.db import models

class Book(models.Model):
    PURCHASE_CHOICES = [('New','New'),('Used','Used')]
    BOOK_TYPE = [('Hardback','Hardback'),('Paperback','Paperback')]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    condition = models.CharField(choices=PURCHASE_CHOICES, max_length=10, blank=True)
    type = models.CharField(choices=BOOK_TYPE, max_length=10)
    published_date=models.DateTimeField()
    cover = models.ImageField(upload_to='uploads/')
    cost = models.FloatField(null=True, blank=True, default=None)
    pages = models.IntegerField(null=True, blank=True, default=None)
    
