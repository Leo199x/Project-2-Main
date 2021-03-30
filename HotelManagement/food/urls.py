from django.urls import path
from .views import (
    checkout,
    IndexView,
    FoodDetailView,
    add_to_cart,
    remove_from_cart,
    # product
)

app_name = "food"
urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('product/<slug>/', FoodDetailView.as_view(), name="product"),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>', remove_from_cart, name='remove-from-cart'),

    # path('products', product, name="product"),
]