from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.ManyToManyField('Address')
    nickname = models.CharField(max_length = 25)
    #creditcard = models.ForeignKey('CreditCard',on_delete=models.CASCADE, null = True)
    def __str__(self):
        return '%s %s' % (self.user, "Profile")


class Address(models.Model):
    HOME = 'home'
    SHIPPING = 'shipping'
    ADDRESS_CHOICES = [(HOME,'home'), (SHIPPING,'shipping')]
    street_addr = models.CharField(max_length = 100)
    apt_suite_unit = models.CharField(max_length = 25,blank = True)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 25)
    zipcode = models.CharField(max_length = 5)
    address_type = models.CharField(max_length = 8, choices = ADDRESS_CHOICES, default = HOME)
    def __str__(self):
        return self.street_addr


class CreditCard(models.Model):
    name = models.CharField(max_length = 100)
    number = models.CharField(max_length = 19)
    expire = models.CharField(max_length = 7)
    code   = models.CharField(max_length = 4)
    zipcode = models.CharField(max_length = 5)
    profile = models.ForeignKey('Profile',on_delete = models.CASCADE,null = True)
    def __str__(self):
        str_len = len(self.number)
        nrem = slice(str_len-4,str_len,1)
        padding = ''
        for i in range (0,str_len - 4) :
            padding += 'x'

        return padding+self.number[nrem]
