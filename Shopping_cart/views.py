from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, reverse
#from .models import Item
from django.utils import timezone
from geekprofile.models import Profile
from details.models import Book
from .models import Order, OrderItem
from django.contrib import messages

class CheckoutView(View):
    model = Book
    template_name = "checkout.html"


def item_list(request):
    context = {
        'items' : Book.objects.all()
    }
    #return render(request, "checkout-page.html", context)
    return render(request, "checkout.html", context)

#def add_to_cart(request, slug):

@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Book, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
    # order_item = OrderItem.objects.create(item=item)

    #check for order
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    print("-------ORDER QUERY SET MADE--------")
    print(order_qs)
    print("-------ORDER QUERY SET MADE--------")


    if order_qs.exists():
        order = order_qs[0]
        #check if order item is in the order
        if order.items.filter(item__slug = item.slug).exists:
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,
                                    ordered_date=ordered_date)
        order.items.add(order_item)
        
    return redirect("book_detail", slug=slug)



    








    


