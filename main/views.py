from django.shortcuts import render, redirect
from .models import Consumption, Food

def index(request):
    if request.method == "POST":
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consumption(user=user, food_consumed=consume)
        consume.save()
        return redirect('index')
    foods = Food.objects.all()
    consumed_food = Consumption.objects.filter(user=request.user)
    return render(request,'main/index.html',{'foods':foods, 'consumed_food':consumed_food})

def delete_food(request, food_id):
    food = Consumption.objects.get(id=food_id)
    if request.method == "POST":
        food.delete()
        return redirect('/')
    return render(request,'main/delete.html')