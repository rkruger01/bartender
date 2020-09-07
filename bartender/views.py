from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Drink

# Create your views here.
def index(request):
    topDrinkList = Drink.objects.order_by('timesMade')[:5]
    context = {"topDrinkList": topDrinkList}
    return render(request, 'bartender/index.html', context)


def drink(request, drinkname):
    if Drink.objects.filter(name=drinkname).exists():
        drink = Drink.objects.get(name=drinkname)
        context = {"requestedDrink":drink}
        return render(request, 'bartender/drink.html', context)