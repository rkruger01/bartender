from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.utils import IntegrityError
from .models import Drink, AlcoholicIngredient, NAIngredient
from .forms import LiquorForm, IngredientForm, UpdateLiquorForm, UpdateNAIngredientForm
import json


# Create your views here.
def index(request):
    topDrinkList = Drink.objects.order_by('timesMade')[:5]
    context = {"topDrinkList": topDrinkList}
    return render(request, 'bartender/index.html', context)


def drink(request, drinkName):
    if Drink.objects.filter(name=drinkName).exists():
        drink = Drink.objects.get(name=drinkName)
        context = {"requestedDrink": drink}
        return render(request, 'bartender/drink.html', context)
    else:
        raise Http404("Error: Drink does not exist")


def search(request):
    def get_queryset():
        query = request.GET.get('search')
        objList = Drink.objects.filter(name__icontains=query)
        return objList

    matches = get_queryset()
    context = {"results": matches}
    print(matches)
    return render(request, 'bartender/results.html', context)


def addLiquor(request):
    if request.method == 'POST':
        form = LiquorForm(request.POST)
        if form.is_valid():
            newAI = AlcoholicIngredient()
            newAI.name = form.cleaned_data['name']
            try:
                newAI.save()
            except IntegrityError:
                return HttpResponse("Error: Drink already exists!")
        return HttpResponseRedirect('/')
    else:
        form = LiquorForm()
        liquorList = AlcoholicIngredient.objects.all()
        context = {'form': form, 'addAlcohol': 'true', 'drinks': liquorList}
    return render(request, 'bartender/addItem.html', context)


def addIngredient(request):
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            newIngredient = NAIngredient()
            newIngredient.name = form.cleaned_data['name']
            try:
                newIngredient.save()
            except IntegrityError:
                return HttpResponse("Error: Ingredient already exists!")
        return HttpResponseRedirect('/')
    else:
        form = IngredientForm()
        objList = NAIngredient.objects.all()
        context = {'form': form, 'ingredients': objList}
    return render(request, 'bartender/addItem.html', context)


def updateMyBar(request):
    if request.method == 'POST':
        #update my ingredients
        aForm = UpdateLiquorForm(request.POST)
        naForm = UpdateNAIngredientForm(request.POST)
        if aForm.is_valid() and naForm.is_valid():
            myList = aForm.cleaned_data.get('liquors')
            aResults = []
            for obj in myList:
                aResults.append(obj.name)
            for aIng in AlcoholicIngredient.objects.all():
                if aIng.name in aResults:
                    aIng.inCabinet = True
                else:
                    aIng.inCabinet = False
                aIng.save()
            myList = naForm.cleaned_data.get('ingredients')
            naResults = []
            for obj in myList:
                naResults.append(obj.name)
            for naIng in NAIngredient.objects.all():
                if naIng.name in naResults:
                    naIng.inCabinet = True
                else:
                    naIng.inCabinet = False
                naIng.save()
        context = {'NAIngredients' : naForm, 'AlcoholicIngredients' : aForm}
    else:
        #list ingredients to be updated
        aIngredientForm = UpdateLiquorForm()
        naIngredientForm = UpdateNAIngredientForm()
        context = {'NAIngredients' : naIngredientForm, 'AlcoholicIngredients' : aIngredientForm}
    return render(request, 'bartender/updateBar.html', context)

# legacy function
def massImportDrinks(request):
    with open("bartender/input.txt", encoding="utf8") as file:
        drinks = json.load(file)
        for drink in drinks:
            newDrink = Drink.objects.create()
            newDrink.name = drink['name']
            for ingredient in drink['ingredients']:
                newIngredient = ""
                if 'ingredient' in ingredient.keys():
                    newIngredient += ingredient['ingredient']
                    if ingredient['ingredient'] in NAIngredient.objects.all().values_list('name', flat=True):
                        newDrink.NAIngredients.add(NAIngredient.objects.get(name__iexact=ingredient['ingredient']))
                    if ingredient['ingredient'] in AlcoholicIngredient.objects.all().values_list('name', flat=True):
                        newDrink.liquor.add(AlcoholicIngredient.objects.get(name__iexact=ingredient['ingredient']))
                    if 'amount' in ingredient.keys():
                        newIngredient += ": " + str(ingredient['amount'])
                    if 'unit' in ingredient.keys():
                        newIngredient += " " + ingredient['unit']
                else:
                    newIngredient += ingredient['special']
                newDrink.ingredientAmount += newIngredient + "\n"
            if 'preparation' in drink.keys():
                newDrink.instructions = drink['preparation']
            else:
                newDrink.instructions = "Mix and Enjoy."
            newDrink.save()
