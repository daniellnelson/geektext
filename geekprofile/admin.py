from django.contrib import admin
from .models import Profile, Address, CreditCard

# Register your models here.

@admin.register(Profile,Address, CreditCard)
class ProfileAdmin(admin.ModelAdmin):
    pass
