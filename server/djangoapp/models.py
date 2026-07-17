from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# 1. Car Make Model
class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name 

# 2. Car Model Model
class CarModel(models.Model):
    # Changed from make_id to car_make for standard Django relational style
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=[("Sedan","SEDAN"), ("SUV","SUV"), ("Wagon","WAGON")])
    year = models.IntegerField(default=2023, validators=[
        MaxValueValidator(2023),
        MinValueValidator(2015)
    ])

    def __str__(self):
        return self.name # FIXED: Matches the exact field name above now   
