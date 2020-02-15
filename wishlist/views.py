from django.shortcuts import render
from django.http import HttpResponse

from .models import Wishlist

def wish_list(request):
    lists = Wishlist.objects.all()
    return render(request, 'wishlist.html', {'lists': lists})
