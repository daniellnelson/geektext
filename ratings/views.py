from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, TemplateView, FormView
from details.models import Book
from .models import Review
from geekprofile.models import Profile
from Shopping_cart.models import Order, OrderItem, Item
from .forms import ReviewForm

def review(request, id):
        template_name = 'write_review.html'
        book = None
        reviews = None

        try:
            book = Book.objects.get(id=id)
            reviews = Review.objects.filter(book=book)
        except Book.DoesNotExist:
            pass

        if request.user.is_authenticated:
            try:
                review = Review.objects.get(book=book, user=request.user)
            except Review.DoesNotExist:
                review = Review(book=book, user=request.user)

            #purchased = Order.objects.filter(user=request.user, Order__items=book).exists()
        else:
            review = None
            #purchased = False

        if request.method == 'POST':
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save()

                return redirect('/details/' + id + '/')
        else:
            form = ReviewForm(instance=review)

        return render(request, template_name, {'book': book, 'reviews': reviews, 'form': form})
