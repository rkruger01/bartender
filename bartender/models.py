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
    name = models.CharField(max_length=60, unique=True)
    liquor = models.ManyToManyField(AlcoholicIngredient)
    NAIngredients = models.ManyToManyField(NAIngredient)
    instructions = models.TextField()
    ingredientAmount = models.TextField()
    timesMade = models.IntegerField(default=0)
    associatedImage = models.URLField(blank=True)