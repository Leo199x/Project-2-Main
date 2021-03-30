from django.db import models
from django.conf import settings
from django.shortcuts import reverse


# Create your models here.


Food_Choices = (
    ('VG','Veg'),
    ('CK', 'Chicken'),
    ('MT', 'Mutton'),
    ('BF', 'Buff'),
    ('TA', 'Tea'),
    ('CF', 'Coffee'),
    ('WN', 'Wine'),
)

class Food(models.Model):
    item_type = models.CharField(choices=Food_Choices, max_length=2)
    name = models.CharField(max_length=20)
    price = models.FloatField()
    discount_price = models.FloatField(blank= True, null= True)
    slug = models.SlugField()
    description = models.TextField()
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('food:product', kwargs={
            'slug': self.slug
        })
    
    def get_add_to_cart_url(self):
        return reverse('food:add-to-cart', kwargs={
        'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse('food:remove-from-cart', kwargs={
        'slug': self.slug
        })



class OrderItem(models.Model): # Items added to the cart
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default= 1)

    def __str__(self):
        return  f'{self.quantity} of {self.food.name} {self.food.get_item_type_display()}'

class Order(models.Model): # shopping cart
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


