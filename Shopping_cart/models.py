from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings
from django.db import models
from geekprofile.models import Profile
from details.models import Book

class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(null=True, blank=True, default=None)
    
    def __str__(self):
        return self.title


class OrderItem(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE)
   



class Order(models.Model):

    #associate the order with a user
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    #items in the order
    items = models. ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    
    #checks if order was ordered
    ordered = models.BooleanField(default=False)
    
  