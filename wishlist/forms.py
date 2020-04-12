from django import forms
from .models import Wishlist

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['listname']

class AddToListForm(forms.Form):
    field = forms.ModelChoiceField(queryset=Wishlist.objects.all())
