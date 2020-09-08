from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.utils import IntegrityError
from .models import Drink, AlcoholicIngredient
from .forms import LiquorForm


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
        context = {'form': form}
    return render(request, 'bartender/addLiquor.html', context)
