from django import template
from Shopping_cart.models import Order

register = template.Library()

@register.filter
def cart_item_count(user):
    if user.is_authenticated: #this might cause a problem
        qs = Order.objects.filter(
            user=user,
            ordered=False
        )
    
        if qs.exists():
            return qs[0].items.count()
    return 1111



