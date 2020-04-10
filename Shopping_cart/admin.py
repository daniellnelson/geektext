from django.contrib import admin
from .models import Order, OrderItem 
    

# Register your models here.
#admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)


