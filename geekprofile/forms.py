from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from geekprofile.models import Profile, Address

class ProfileRegisterForm(UserCreationForm):
    email = forms.EmailField()
    nickname = forms.CharField(max_length = 25)
    street_addr = forms.CharField(max_length = 100)
    apt_suite_unit = forms.CharField(max_length = 25)
    city = forms.CharField(max_length = 50)
    state = forms.CharField(max_length = 25)
    zipcode = forms.CharField(max_length = 5)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email',
                  'nickname','street_addr','apt_suite_unit',
                  'city', 'state','zipcode']

#def save(self, commit = True):

#    return p


#this inherits from UserCreationForm and adds the email fields
