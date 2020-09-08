from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index,name="Index"),
    url(r'search/', views.search, name="Search Results"),
    url(r'^(?P<drinkName>[a-zA-Z0-9]+)/?$', views.drink, name="Drink"),
    url(r'^add-liquor/?$', views.addLiquor, name="Add Liquor")
]