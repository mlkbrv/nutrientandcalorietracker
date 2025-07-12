from django.contrib.auth.models import User
from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    carbohydrates = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()

    def __str__(self):
        return self.name

class Consumption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_consumed = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.food_consumed.name}'