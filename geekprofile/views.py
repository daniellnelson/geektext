from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from geekprofile.forms import ProfileRegisterForm, UserUpdateForm, ProfileUpdateForm, AddressUpdateForm
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

def profile_edit(request):
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, instance = request.user.profile)
        a_form = AddressUpdateForm(request.POST, instance = request.user.profile.home_address.get())
        if u_form.is_valid() and p_form.is_valid() and a_form.is_valid():
            u_form.save()
            p_form.save()
            a_form.save()
        return redirect('profile_detail')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
        a_form = AddressUpdateForm(instance = request.user.profile.home_address.get())
    context = {
        'u_form': u_form,
        'p_form': p_form,
        'a_form': a_form
    }
    return render(request, 'profile_edit.html',context)
    #HttpResponse('<p>Profile with the id {}</p>'.format(id))
