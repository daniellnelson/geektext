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


def add_to_cart(request, slug):
    item = get_object_or_404(Book, slug=Book.slug)
    order_item = OrderItem.objects.create(item=item)

    #check for order
    order_qs= Order.objects.filter(user=request.user, ordered=False)
    if(order_qs).exists:
        order = order_qs[0]

        #check if order item is in the order
        if order.items.filter(item__slug = item.slug.exists):
            order_item.quantity += 1
            order_item.save()
        else:
            ordered_date = timezone.now()
            order = order.objects.create(user=request.user,ordered_date=ordered_date)
            order.items.add(order_item)
        
        #return redirect("book_detail", slug=slug)
        return reverse("book_detail", kwargs={
            'slug' : slug
        })









    


