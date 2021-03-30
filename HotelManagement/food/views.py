from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.utils import timezone
from .models import Food, OrderItem, Order


# Create your views here.

def food_list(request):
    return render(request, "food/food_list.html", context={
        'foods': Food.objects.all()
    })

def checkout(request):
    return render(request, 'food/checkout.html')    

class IndexView(ListView): # passed as object_list
    model = Food
    template_name = 'food/home-page.html'

# def index(request):
#     return render(request, 'food/home-page.html', context={
#         'foods': Food.objects.all()
#     })


# def product(request):
#     return render(request, 'food/product-page.html')
class FoodDetailView(DetailView): # passed as object
    model = Food
    template_name = 'food/product-page.html'

"""
A function will take the food
create an order item 
assign the order item to the order if the user has no order it will be created at the spot
when we remove the food it will remove the orderitem from the order's items field 
"""
def add_to_cart(request, slug):
    food = get_object_or_404(Food, slug= slug)
    order_item, created = OrderItem.objects.get_or_create(
        food=food,
        user= request.user,
        ordered=False)
    order_qs = Order.objects.filter(user = request.user, ordered= False)  
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(food__slug= food.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This food quantity was updated to your cart")
        else:
            messages.info(request, "This food was added to your cart")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date= ordered_date)
        order.items.add(order_item)
        messages.info(request, "This food was added to your cart")
    return redirect("food:product", slug= slug)

def remove_from_cart(request, slug):
    food = get_object_or_404(Food, slug= slug)
    order_qs = Order.objects.filter(user = request.user, ordered= False)  
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(food__slug= food.slug).exists():
            order_item = OrderItem.objects.filter(
                                food=food,
                                user= request.user,
                                ordered=False
                                )[0]
            order.items.remove(order_item)
            messages.info(request, "This food was removed from your cart")
            return redirect('food:product', slug= slug)
        else:
            messages.info(request, "This food wasn't in your cart")
            return redirect('food:product', slug= slug)

    else:
        messages.info(request, "You don't have an active order")
        return redirect('food:product', slug= slug)
    



