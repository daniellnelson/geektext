from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import reverse
from .models import Book


#Old Function-based views

"""
def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        raise Http404('Book Not Found')
    return render(request, 'book_detail.html', {'book': book})
    """
#New Class-based Views

class HomeView(ListView):
    model = Book
    template_name = 'home.html'


class BookView(DetailView):
    model = Book
    template_name = 'book_detail.html'

"""def add_to_cart(request, slug):
    item = get_object_or_404(Book, slug=Book.slug)
    order_item = OrderItem.objects.create(item=item)

    #check for order
    order_qs= Order.objects.filter(user=request.user, is_ordered=False)
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
        
        return redirect("book_detail", slug=slug)"""



    


  


   
    
