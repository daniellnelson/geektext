from django import forms
from .models import Wishlist

class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = ['listname']

class AddToListForm(forms.Form):
    field = forms.ModelChoiceField(queryset=Wishlist.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AddToListForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['field'].queryset = Wishlist.objects.filter(user=user)

class MoveToListForm(forms.Form):
    field = forms.ModelChoiceField(queryset=Wishlist.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MoveToListForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['field'].queryset = Wishlist.objects.filter(user=user)
