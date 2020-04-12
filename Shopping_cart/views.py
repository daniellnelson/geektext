from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, reverse
from django.contrib import messages
#from .models import Item
from django.utils import timezone
from geekprofile.models import Profile
from details.models import Book
from .models import Order, OrderItem
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist


class CartView(LoginRequiredMixin,View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(
                user=self.request.user,
                ordered=False
            )
            context = {

                'object': order

            }
            return render(self.request, 'checkout.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")


class OrderSummaryView(LoginRequiredMixin,View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(
                user=self.request.user,
                ordered=False
            )
            context = {
                'object': order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")
        


def item_list(request):
    context = {
        'items' : Book.objects.all()
    }
    return render(request, "checkout.html", context)

@login_required
def remove_from_cart(request,slug):
    #getting the item
    item = get_object_or_404(Book, slug=slug)

    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )

    #checking if the user has an order
    if order_qs.exists(): #if they do

        order = order_qs[0] #grab that shit

        #check if order item is in the order
        if order.items.filter(item__slug = item.slug).exists:
            try:
                order_item = OrderItem.objects.filter(
                    item=item, 
                    user=request.user,
                    ordered=False
                )[0]
                order.items.remove(order_item)
                order_item.delete()
            except IndexError:
                messages.info(request, "Nothing is in your Order: Add an Item to your Order before removing!")
            except:
                messages.info(request, "Internal error...redirecting")
                return redirect("book_detail", slug=slug)

            messages.info(request, "This item was removed from your cart.")
            return redirect("book_detail", slug=slug)

        else:
            #add a message saying the order does not contain the item
            messages.info(request, "This order does not contain the item!")
            return redirect("book_detail", slug=slug)

    else:
        #add a message saying the user does have an order
        messages.info(request, "You do not have an order!")
        return redirect("book_detail", slug=slug)


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Book, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item, 
            user=request.user,
             ordered=False)

    #check for order
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        print("-----ORDER EXISTS-----")
        order = order_qs[0]
        #check if order item is in the order
        if order.items.filter(item__slug = item.slug).exists:
            print("ORDER ITEM FILTER EXISTS")
            order_item.quantity += 1
            print("QUANTITY UPDATED TO", order_item.quantity)      
            order_item.save()
            print("ORDER ITEM SAVED")
            order.items.add(order_item)
            print("ADDED TO ORDER")  
            messages.info(request, "This item quantity has been updated")
            for item in order.items.all() :
                print("ADD-TO-CART FUNC: Current Order", item)
            return redirect("book_detail", slug=slug)

        else:
            print("ADDING TO A NEW ORDER")          
            order.items.add(order_item)
            print("ORDER ITEM ADDED WITH QUERYSET EXIST: ", order_item)
            messages.info(request, "This item has been added to your cart")
            for item in order.items.all():
                print("ADD-TO-CART FUNC: Current Order", item)
            return redirect("book_detail", slug=slug)

        

    else:
        print("NO ORDER EXISTS---CREATING ORDER")
        ordered_date = timezone.now()

        order = Order.objects.create(user=request.user,
                                    ordered_date=ordered_date)
        print("ORDER CREATED")   
        order.items.add(order_item)

        print("ORDER ITEM ADDED QUERYSET DIDNT EXIST: ", order_item)
        print("ADD-TO-CART FUNC: Current Order", order)

        
        messages.info(request, "This item has been added to your cart")
        return redirect("book_detail", slug=slug)
        
        
    return redirect("book_detail", slug=slug)








    








    


