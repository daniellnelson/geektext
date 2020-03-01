from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileRegisterForm
from .models import Profile

#create views
def profile_signup(request):
    if request.method=='POST':
        form = ProfileRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('profile_login')
    else:
        form = ProfileRegisterForm()
    return render(request, 'profile_signup.html',{'form':form})

def profile_detail(request):
    return render(request, 'profile_home.html')
    #HttpResponse('<p>Profile with the id {}</p>'.format(id))
