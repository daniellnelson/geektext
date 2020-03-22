from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Item
def item_list(request):
    context = {
        'items' : Item.objects.all()
    }
    #return render(request, "checkout-page.html", context)
    return render(request, "checkout.html", context)