from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings
from django.db import models
from django.db.models import Sum
from geekprofile.models import Profile  #Use from geekprofile
from details.models import Book       #Use from details
from django.shortcuts import reverse
from django.http import HttpResponse



class Item(models.Model):
    title = Book.title
    price = Book.cost
    isbn  = Book.ISBN
    slug  = Book.slug

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("geektext:book_detail", kwargs={
            'slug': self.slug
        })
    def get_add_to_cart_url(self):
        return reverse("geektext:add-to-cart", kwargs={
            'slug': self.slug
        })
    def get_remove_from_cart_url(self):
        return reverse("geektext:remove-from-cart", kwargs={
            'slug': self.slug
        })

class OrderItem(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                 on_delete=models.CASCADE, blank=True, null=True)
                 
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Book,on_delete=models.CASCADE)
   
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"
    
    def get_total_item_price(self):
        return self.quantity * self.item.cost

    

class Order(models.Model):

    #associate the order with a user

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    #items in the order
    items = models.ManyToManyField(OrderItem)
    
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    
    #checks if order was ordered
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()

        formatted_float = "{:.2f}".format(total)  
        return formatted_float