from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<p>PROFILE VIEW</p>')
def profile_detail(request, id):
    return HttpResponse('<p>Profile with the id {}</p>'.format(id))
    
