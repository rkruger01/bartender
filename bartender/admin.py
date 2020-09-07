from django.contrib import admin

# Register your models here.

from .models import Drink, AlcoholicIngredient, NAIngredient

admin.site.register(Drink)
admin.site.register(AlcoholicIngredient)
admin.site.register(NAIngredient)