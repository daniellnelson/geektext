from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from geekprofile.forms import ProfileRegisterForm
from geekprofile.models import Profile, Address
from django.contrib.auth.models import User

#create views
def profile_signup(request):
    if request.method=='POST':
        form = ProfileRegisterForm(request.POST)
        if form.is_valid():
            u = User()
            u = form.save()
            u.save()
            a = Address()
            username = form.cleaned_data.get('username')
            p = Profile.objects.filter(user=u)[0]
            p.nickname = form.cleaned_data.get('nickname')
            a.street_addr = form.cleaned_data.get('street_addr')
            a.apt_suite_unit = form.cleaned_data.get('apt_suite_unit')
            a.city = form.cleaned_data.get('city')
            a.state = form.cleaned_data.get('state')
            a.zipcode = form.cleaned_data.get('zipcode')
            a.save()
            p.home_address.add(a)
            p.save()
            
            return redirect('profile_login')
    else:
        form = ProfileRegisterForm()
    return render(request, 'profile_signup.html',{'form':form})

def profile_detail(request):
    return render(request, 'profile_home.html')
    #HttpResponse('<p>Profile with the id {}</p>'.format(id))
