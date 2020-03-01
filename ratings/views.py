from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import Http404

from details.models import Book
from .models import Rating, Comment
from .forms import CommentForm, RateForm


def rate_book(request, id):
    book = get_object_or_404(Book, id=id)
    rate = None
    if request.method == 'POST':
        rate_form = RateForm(request.POST)
        if rate_form.is_valid():
            rate = rate_form.save(commit=False)
            rate.book = book
            rate.save()

            return redirect('/details/' + id + '/')

    else:
        rate_form = RateForm(request.POST)

    context = {
        "book": book,
        "rate": rate,
        "rate_form": rate_form
    }

    return render(request, "rate_book.html", context)

# Create your views here.
def display_comment(request, id):
    book = get_object_or_404(Book, id=id)
    comments = Comment.objects.all()
    return render(request, 'book_reviews.html', {'book': book, 'comments': comments})

def write_comment(request, id):
    book = get_object_or_404(Book, id=id)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():

            # create comment object but dont save to database yet
            new_comment = comment_form.save(commit=False)
            # assign the current post to the comment
            new_comment.book = book
            #add time
            #new_comment.date = timezone.now
            # save the comment to the database
            new_comment.save()

            return redirect('/details/' + id + '/')
    else:
        comment_form = CommentForm(request.POST)

    context = {
        "book": book,
        "comment_form": comment_form,
        "new_comment": new_comment,
    }

    return render(request, "write_review.html", context)

def rem_comment(request):
    id = str(comment.book.id)
    comment.delete()
    return redirect('/details/' + id + '/')

def approve_comment(request):
    id = str(comment.book.id)
    comment.approve()
    return redirect('/details/' + id + '/')
