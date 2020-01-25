from django.db import models

class Book(models.Model):
    PURCHASE_CHOICES = [('N','New'),('U','Used')]
    BOOK_TYPE = [('H','Hardback'),('P','Paperback')]
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    genre = models.CharField(max_length=30)
    condition = models.CharField(choices=PURCHASE_CHOICES, max_length=1, blank=True)
    type = models.CharField(choices=BOOK_TYPE, max_length=1)
    published_date=models.DateTimeField()
    
