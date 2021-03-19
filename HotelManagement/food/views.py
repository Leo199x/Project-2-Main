from django.shortcuts import render
from .models import Food

# Create your views here.

def food_list(request):
    return render(request, "food/food_list.html", context={
        'foods': Food.objects.all()
    })

