from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.ManyToManyField('Address')
    nickname = models.CharField(max_length = 25)
    creditcard = models.ForeignKey('CreditCard',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user.username} Profile"


class Address(models.Model):
    street_addr = models.CharField(max_length = 100)
    apt_suite_unit = models.CharField(max_length = 25,blank = True)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 25)
    zipcode = models.CharField(max_length = 5)

class CreditCard(models.Model):
    name = models.CharField(max_length = 100)
    number = models.CharField(max_length = 16)
    expire = models.CharField(max_length = 7)
    code   = models.CharField(max_length = 4)
    zipcode = models.CharField(max_length = 5)
