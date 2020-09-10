from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name="Index"),
    url(r'search/', views.search, name="Search Results"),
    url(r'^add-liquor/?$', views.addLiquor, name="Add Liquor"),
    url(r'^add-ingredient', views.addIngredient, name="Add Ingredient"),
    url(r'^(?P<drinkName>[a-zA-Z0-9_ ]+)/?$', views.drink, name="Drink"),
]