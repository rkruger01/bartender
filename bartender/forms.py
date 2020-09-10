from django import forms
from .models import AlcoholicIngredient, NAIngredient


class LiquorForm(forms.Form):
    name = forms.CharField(label='Liquor Name', max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))


class IngredientForm(forms.Form):
    name = forms.CharField(label='Ingredient Name', max_length=60,
                           widget=forms.TextInput(attrs={'class': 'form-control'}))


class UpdateLiquorForm(forms.Form):
    liquors = forms.ModelMultipleChoiceField(
        queryset=AlcoholicIngredient.objects.all().order_by('name'),
        widget=forms.CheckboxSelectMultiple(attrs={'class':"form-check-input"}),
        initial=[liquor.id for liquor in AlcoholicIngredient.objects.filter(inCabinet=True)]
    )


class UpdateNAIngredientForm(forms.Form):
    ingredients = forms.ModelMultipleChoiceField(
        queryset=NAIngredient.objects.all().order_by('name'),
        widget=forms.CheckboxSelectMultiple(attrs={'class':"form-check-input"}),
        initial=[ing.id for ing in NAIngredient.objects.filter(inCabinet=True)],
    )
