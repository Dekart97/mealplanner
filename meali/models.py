from django.db import models

from django.db import models

class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    time = models.IntegerField()
    steps = models.IntegerField()
    step = models.IntegerField()

    def __str__(self):
        return self.name
    
class Meals(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.URLField(max_length=200)
    time = models.IntegerField()

    def __str__(self):
        return self.name 