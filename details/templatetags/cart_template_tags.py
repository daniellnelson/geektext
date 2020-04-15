from django import template
from Shopping_cart.models import Order, OrderItem
register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated: #this might cause a problem
        print("USER AUTHENTICATED!")
        print("AUTHENTICATED USER:  ",user.username)
        qs = Order.objects.filter(
            user=user,
            ordered=False
        )



        for order_item in qs:
            print("ORDER ITEM:          ",order_item)
        print("PRINTED QUERYSET:    ",qs[0].items)
    
        if qs.exists():
            print("QUERYSET EXISTS!!")
            print("QUERYSET ITEMS", qs[0].items)
            return qs[0].items.count()

            
    return 10