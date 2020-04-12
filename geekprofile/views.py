import re
from django import forms
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from geekprofile.forms import (ProfileRegisterForm, UserUpdateForm,
                ProfileUpdateForm, AddressUpdateForm)
from geekprofile.models import Profile, Address, CreditCard
from django.contrib.auth.models import User
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


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
            messages.success(request, f'Profile has been created.')
            return redirect('profile_login')
    else:
        form = ProfileRegisterForm()
    return render(request, 'profile_signup.html',{'form':form})

@login_required
def profile_detail(request):
    context = CreditCard.objects.filter(profile = request.user.profile)
    return render(request, 'profile_home.html', {'context':context})

@login_required
def profile_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user = user.request,data = request.POST)
        if form.is_valid():
            messages.success(request, f'Password has changed.')
            form.save()
            update_session_auth_hash(request, form.user)
            redirect('profile_home.html')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'profile_password.html')

@login_required
def profile_edit(request):
    a_formset = modelformset_factory(Address, fields = ('street_addr','apt_suite_unit',
        'city','state','zipcode','address_type'), extra = 1, can_delete = True)
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, instance = request.user.profile)
        a_form = a_formset(request.POST)


        if u_form.is_valid() and p_form.is_valid() and a_form.is_valid():
            messages.success(request, f'Information has been updated.')
            u_form.save()
            p_form.save()
            instances = a_form.save()
            if len(instances) > 0 :
                request.user.profile.home_address.add(instances[0])
        return redirect('profile_detail')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
        a_form = a_formset(queryset = request.user.profile.home_address.all())



    context = {
        'u_form': u_form,
        'p_form': p_form,
        'a_form': a_form,
        }
    return render(request, 'profile_edit.html',context)

@login_required
def profile_cards(request):

    cformset = modelformset_factory(CreditCard, fields = ('number','expire','code', 'zipcode'),can_delete = True )
    p = request.user.profile
    cardset = CreditCard.objects.filter(profile = p)

    if request.method == 'POST':
        cform = cformset(request.POST)

        if cform.is_valid():
            mmyyyy = re.compile('^[0-1][0-9]/[0-9]{4}$')
            zip = re.compile('[0-9]{5}')
            ccv = re.compile('^[0-9]{3,4}$')
            num_pattern = re.compile('^[0-9]{12,19}$')
            no_error_flag = True
            for form in cform:
                if form.has_changed():
                    fc = form.cleaned_data.get('number')
                    expire = form.cleaned_data.get('expire')
                    code = form.cleaned_data.get('code')
                    zipcode = form.cleaned_data.get('zipcode')
                    if not (mmyyyy.match(expire) and ccv.match(code) and zip.match(zipcode) and num_pattern.match(fc)):
                        #raise forms.ValidationError(_('Invalid data'))
                        messages.error(request, f'Error check the card information')
                        no_error_flag = no_error_flag and False
            if no_error_flag:
               instances = cform.save()
               messages.success(request, f'Credit cards have been updated.')
               for cc in instances:
                   cc.profile = p
                   cc.save()

            return redirect('profile_cards')
        else:
            messages.error(request, f'Error check the information typed.')


    else:
            cform = cformset(queryset = cardset)


    context = {'cform':cform}
    return render(request, 'creditcard.html', context )
