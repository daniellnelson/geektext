from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .forms import WishlistForm, AddToListForm, MoveToListForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Wishlist
from details.models import Book

@login_required
def all_wish_list(request):
    lists = Wishlist.objects.filter(user=request.user)
    bookobject = Book.objects.all()
    return render(request, 'wishlist.html', {'lists': lists})

@login_required
def current_wish_list(request, id):
    try:
        list = Wishlist.objects.get(id=id)
    except Wishlist.DoesNotExist:
        raise Http404('WishList Not Found')
    lists = Wishlist.objects.filter(user=request.user)
    bookobject = Book.objects.all()
    return render(request, 'wishlist/current.html', {'list': list})

@login_required
def create_wish_list(request):
    lists = Wishlist.objects.filter(user=request.user)
    if lists.count() == 3:
        messages.error(request, "Only 3 wishlists are allowed per user account.")
        return redirect('all_wish_list')
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

@login_required
def delete_wish_list(request, id):
    list = Wishlist.objects.get(id=id)
    if request.method == 'POST':
        list.delete()
        messages.success(request, "Your wishlist has been successfully deleted.")
        return redirect('all_wish_list')

@login_required
def add_to_list(request, id):
    bookobject = Book.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'wishlist/add.html', {'form': AddToListForm(user=request.user)})
    else:
        form = AddToListForm(request.POST)
        if form.is_valid():
            list = form.cleaned_data['field']
            list.user = request.user
            list.books.add(bookobject)
            return redirect('current_wish_list', list.id)

@login_required
def delete_book(request, bookid, wishid):
    bookobject = Book.objects.get(id=bookid)
    list = Wishlist.objects.get(id=wishid)
    if request.method == 'POST':
        list.books.remove(bookobject)
        return redirect('current_wish_list', list.id)

@login_required
def move_book(request, bookid, wishid):
    bookobject = Book.objects.get(id=bookid)
    list = Wishlist.objects.get(id=wishid)
    if request.method == 'GET':
        return render(request, 'wishlist/move.html', {'form': MoveToListForm(user=request.user)})
    else:
        list.books.remove(bookobject)
        form = MoveToListForm(request.POST)
        if form.is_valid():
            list = form.cleaned_data['field']
            list.user = request.user
            list.books.add(bookobject)
            return redirect('current_wish_list', list.id)
