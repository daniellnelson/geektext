from django import template
from Shopping_cart.models import Order, OrderItem
register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated: #this might cause a problem
        print("USER AUTHENTICATED!")
        qs = Order.objects.filter(
            user=user,
            ordered=False
        )

        for order_item in qs:

            print(order_item)

        print(user.username)
        print(qs)
    
        if qs.exists():
            print("QUERYSET EXISTS!!")
            print("COUNT---", qs[0].items.count())
            return qs[0].items.count()

            
    return 10