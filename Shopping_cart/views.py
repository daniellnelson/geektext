from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, View
from django.shortcuts import redirect
from .models import Item
from geekprofile.models import Profile
from details.models import Book
from .models import Order, OrderItem

class CheckoutView(View):
    model = Book
    template_name = "checkout.html"



def item_list(request):
    context = {
        'items' : Book.objects.all()
    }
    return render(request, "checkout.html", context)

def add_to_cart(request, slug):
    item = get_object_or_404(Book, slug=Book.slug)
    order_item = OrderItem.objects.create(item=slug)

    #check for order
    order_qs= Order.objects.filter(user=request.user, is_ordered=False)
    if(order_qs).exists:
        order = order_qs[0]

        #check if order item is in the order
        if order.items.filter(item_slug = item.slug.exists):
            order_item.quantity += 1
            order_item.save()
        else:
            order = order.objects.create(user=request.user)
            order.items.add(order_item)
        
        return redirect("geektext:book_detail", kwargs={
            'slug' : slug
        })
    











    


