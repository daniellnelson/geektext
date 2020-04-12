from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from .models import Book
from .models import Author

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        raise Http404('Book Not Found')
    return render(request, 'book_detail.html', {'book': book})

def author_books(request, id):
    try: 
        author = Author.objects.get(id=id)  
        books = Book.objects.filter(author=author) 
    except Author.DoesNotExist:
        raise Http404('Author Not Found')
    return render(request, 'author_books.html', {'books': books})