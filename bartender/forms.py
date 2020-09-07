from django import forms
from .models import AlcoholicIngredient


class LiquorForm(forms.Form):
    name = forms.CharField(label='Liquor Name', max_length=60)
