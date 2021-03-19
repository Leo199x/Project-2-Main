from django.contrib import admin
from .models import Food, OrderItem, Order


class FoodAdmin(admin.ModelAdmin):
    list_display = ("item_type","name", "price")
class OrderAdmin(admin.ModelAdmin):
    # list_display = ("category", "ordered", "price", "quantity", "ordered_on")
    list_display = ("category",)

    def category(self, obj):
        category = obj.food.item_type
        return category

    # def ordered(self, obj):
    #     ordered = obj.order.name
    #     return ordered

    # def price(self, obj):
    #     price = obj.order.price
    #     return price

# Register your models here.
admin.site.register(Food, FoodAdmin)
admin.site.register(OrderItem, OrderAdmin)
admin.site.register(Order)