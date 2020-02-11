from django.shortcuts import render
from django.http import HttpResponse
from details.models import Book

def home(request):
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def profile_detail(request, id):
    return HttpResponse('<p>Profile with the id {}</p>'.format(id))

def book_detail(request, id):
    try:
        book = Book.objects.get(id=id)
    except Book.DoesNotExist:
        raise Http404('Book Not Found')
    return render(request, 'book_detail.html', {'book': book})
