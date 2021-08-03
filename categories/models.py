from django.db import models
from assets.models import Vehicle, Finance, Computer, Laptop

# Create your models here.
class Transport(models.Model):
    vehicles = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.vehicles