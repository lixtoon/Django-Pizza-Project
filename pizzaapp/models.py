from django.db import models

# Create your models here.
FOOD_TYPE = (
    ('Burger','Burger'),
    ('Sandwich','Sandwich'),
    ('Pizza','Pizza'),
)
class FoodModel(models.Model):
    name = models.CharField(max_length=35)
    type = models.CharField(max_length=10, choices=FOOD_TYPE)
    price = models.CharField(max_length=100)
class PizzaModel(models.Model):
    name = models.CharField( max_length=20)
    price = models.CharField(blank=True, max_length=100)
