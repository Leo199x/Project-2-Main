from django.db import models
from django.conf import settings


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

    def __str__(self):
        return self.name



class OrderItem(models.Model): # Items added to the cart
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return  {self.food.name}

class Order(models.Model): # shopping cart
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

