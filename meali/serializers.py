from rest_framework import serializers
from .models import MealPlan
from .models import Meals

class MealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealPlan
        fields = '__all__'

class MealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meals
        fields = '__all__'
