from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('anonymous', 'rating', 'comment',)
        widgets = {
            'anonymous': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'rating': forms.Select(attrs={'class':  'form-control'}, choices=(
                (None, 'None'),
                (1, 'Poor (1)'),
                (2, 'Average (2)'),
                (3, 'Good (3)'),
                (4, 'Very Good (4)'),
                (5, 'Excellent (5)')
            )),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }
