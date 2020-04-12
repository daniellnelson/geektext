from django import forms
from django.forms import BaseModelFormSet
from django.forms.widgets import TextInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from geekprofile.models import Profile, Address, CreditCard


class ProfileRegisterForm(UserCreationForm):
    email = forms.EmailField()
    nickname = forms.CharField(max_length = 25)
    street_addr = forms.CharField(max_length = 100)
    apt_suite_unit = forms.CharField(max_length = 25, required = False)
    city = forms.CharField(max_length = 50)
    state = forms.CharField(max_length = 25)
    zipcode = forms.CharField(max_length = 5)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email',
                  'nickname','street_addr','apt_suite_unit',
                  'city', 'state','zipcode']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname']


class AddressUpdateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street_addr','apt_suite_unit',
            'city','state','zipcode','address_type']






    #card_number = CreditCardField(placeholder=u'0000 0000 0000 0000', min_length=13, max_length=19)
