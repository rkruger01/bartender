from django import forms
from .models import AlcoholicIngredient


class LiquorForm(forms.Form):
    name = forms.CharField(label='Liquor Name', max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))


class IngredientForm(forms.Form):
    name = forms.CharField(label='Ingredient Name', max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))

