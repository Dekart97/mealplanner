from django.urls import path
from .views import MealPlanList
from .views import MealsList

urlpatterns = [
    path('mealplans/', MealPlanList.as_view(), name='mealplan-list'),
    path('meals/', MealsList.as_view(), name='meals-list'),
]