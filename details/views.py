from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        raise Http404('Book Not Found')
    return render(request, 'book_detail.html', {'book': book})
   
    
