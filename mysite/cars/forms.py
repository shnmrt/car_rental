from django import forms
from .models import Review
from django.forms import ModelForm

"""
class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    review = forms.CharField(
        label='Please write your review here', 
        max_length=250, 
        widget=forms.Textarea(attrs={'class':'myform', 'rows':'10','cols':'50'})
    )
"""

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name','last_name', 'stars']