from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileRegisterForm

#create views
def profile_detail(request):
    if request.method=='POST':
        form = ProfileRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('home')
    else:
        form = ProfileRegisterForm()
    return render(request, 'profile_home.html',{'form':form})

    #HttpResponse('<p>Profile with the id {}</p>'.format(id))
