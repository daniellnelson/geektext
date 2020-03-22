from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import WishlistForm

from .models import Wishlist
from details.models import Book


def all_wish_list(request):
    lists = Wishlist.objects.all()
    bookobject = Book.objects.all()
    return render(request, 'wishlist.html', {'lists': lists})

def current_wish_list(request, id):
    try:
        list = Wishlist.objects.get(id=id)
    except Wishlist.DoesNotExist:
        raise Http404('WishList Not Found')
    lists = Wishlist.objects.all()
    bookobject = Book.objects.all()
    return render(request, 'wishlist/current.html', {'list': list})

def create_wish_list(request):
    if request.method == 'GET':
        return render(request, 'wishlist/create.html', {'form': WishlistForm()})
    else:
        try:
            form = WishlistForm(request.POST)
            newlist = form.save(commit=False)
            newlist.user = request.user
            newlist.save()
            return redirect('wishlist.html')
        except ValueError:
            return render(request, 'wishlist/create.html', {'form': WishlistForm(), 'error':'Bad data passed in. Try again.'})
