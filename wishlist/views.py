from django.shortcuts import render
from django.http import HttpResponse
from .forms import WishlistForm

from .models import Wishlist

def all_wish_list(request):
    lists = Wishlist.objects.filter(user=request.user)
    return render(request, 'wishlist.html', {'lists': lists})

def current_wish_list(request):
    pass

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
