from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import reverse
from .models import Book
from .models import Author


#Old Function-based views


def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        raise Http404('Book Not Found')
    return render(request, 'book_detail.html', {'book': books})

def author_books(request, id):
    try: 
        author = Author.objects.get(id=id)  
        books = Book.objects.filter(author=author) 
    except Author.DoesNotExist:
        raise Http404('Author Not Found')
    return render(request, 'author_books.html', {'books': books})



#New Class-based Views

class HomeView(ListView):
    model = Book
    template_name = 'home.html'
    


class BookView(DetailView):
    model = Book
    template_name = 'book_detail.html'




    


  


   
    
