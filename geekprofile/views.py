from django.shortcuts import render
from django.http import HttpResponse

#create views
def profile_detail(request, id):
    return HttpResponse('<p>Profile with the id {}</p>'.format(id))
