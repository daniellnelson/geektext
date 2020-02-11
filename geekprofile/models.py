from django.db import models

class User(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 50)
    email    = models.EmailField(blank = False)
    home_address = models.ManyToManyField('Address', null = False)
    nickname = models.CharField(max_length = 25)
    creditcard = models.ForeignKey('CreditCard',on_delete=models.CASCADE)
    
    
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
    