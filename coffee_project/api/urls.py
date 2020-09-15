from django.urls import path, include
from .views import AllCoffeeMachines, AllCoffeePods


urlpatterns = [
    path('all-coffee-machines', AllCoffeeMachines.as_view()),
    path('all-coffee-pods', AllCoffeePods.as_view())
]
