from django.db import models


# Create your models here.
vehicle_weight = (
    ("Heavy vehicle", "Heavy vehicle"),
    ("Light vehicle", "Light vehicle"),
)

vehicle_brand = (
    ("Toyota", "Toyota"),
    ("Audi", "Audi"),
    ("Nissan", "Nissan"),
    ("Mercedes", "Mercedes"),
    ("Vox Wagon", "Vox Wagon"),
    ("BMW", "BMW"),
    ("Range Rover", "Range Rover"),
)

computer_brand = (
    ("Hp", "Hp"),
    ("Del", "Del"),
    ("Toshiba", "Toshiba")
)

computer_memory = (
    ("500 Gb", "500 Gb"),
    ("1 Tb", "1 Tb")
)

preprosser = (
    ("Core i3", "Core i3"),
    ("Core i5", "Core i5"),
    ("Core i7", "Core i7"),
)

class Vehicle(models.Model):
    name = models.CharField(max_length=30)
    weight_class = models.CharField(max_length=30, choices=vehicle_weight)
    vehicle_brand = models.CharField(max_length=30, choices=vehicle_brand)

    def __str__(self) -> str:
        return self.name
    
    
class Computers(models.Model):
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=20, choices=computer_brand)
    memory = models.CharField(max_length=15, choices=computer_memory)
    preprosser = models.CharField(max_length=15, choices=preprosser)

    def __str__(self) -> str:
        return self.name


