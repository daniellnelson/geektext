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


class OrderItem(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    #item = models.ForeignKey(Book, on_delete=models.CASCADE)
    #item = models.ForeignKey(Book,on_delete=models.CASCADE)

    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    item = models.OneToOneField(Book, on_delete=models.SET_NULL, null=True)
    
    #ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    quantity = models.IntegerField(default=1)

    """def __str__(self):
        return f"{self.quantity} of { Book.title }"""

    def __str__(self):
    
        return self.item.name

class Order(models.Model):

    #associate the order with a user
    #ref_code = models.CharField(max_length=15, null=True)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    
    #items in the order
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    
    #checks if order was ordered
    ordered = models.BooleanField(default=False)

    def get_cart_items(self):
        return self.items.all()
    
    def get_cart_total(self):
        return sum([item.product.price for item in self.items.all()])

    def __str__(self):
        return self.user.username


    
    

