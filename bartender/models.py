from django.db import models


# Create your models here.
class AlcoholicIngredient(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class NAIngredient(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name


class Drink(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=60, unique=True)
    liquor = models.ManyToManyField(AlcoholicIngredient, verbose_name="Alcoholic Ingredients")
    NAIngredients = models.ManyToManyField(NAIngredient, verbose_name="Non-Alcoholic Ingredients")
    instructions = models.TextField(verbose_name="Instructions")
    ingredientAmount = models.TextField(verbose_name="Ingredient Amount")
    timesMade = models.IntegerField(default=0, verbose_name="Times Made")
    associatedImage = models.URLField(blank=True, verbose_name="Associated Image")
