from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import WishlistForm, AddToListForm

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
            return redirect('current_wish_list', newlist.id)
        except ValueError:
            return render(request, 'wishlist/create.html', {'form': WishlistForm(), 'error':'Bad data passed in. Try again.'})

def add_to_list(request, id):
    bookobject = Book.objects.get(id=id)
    lists = Wishlist.objects.all()
    if request.method == 'GET':
        return render(request, 'wishlist/add.html', {'lists': lists, 'form': AddToListForm()})
    else:
        form = AddToListForm(request.POST)
        if form.is_valid():
            list = form.cleaned_data['field']
            list.user = request.user
            list.books.add(bookobject)
            return redirect('current_wish_list', list.id)
