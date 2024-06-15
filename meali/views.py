from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MealPlan
from .models import Meals
from .serializers import MealPlanSerializer
from .serializers import MealsSerializer

class MealPlanList(APIView):
    def get(self, request):
        mealplans = MealPlan.objects.all()
        serializer = MealPlanSerializer(mealplans, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MealPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MealsList(APIView):
    def get(self, request):
        meals = Meals.objects.all()
        serializer = MealsSerializer(meals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MealsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


