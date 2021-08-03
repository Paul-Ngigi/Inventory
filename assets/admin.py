from django.contrib import admin
from .models import Vehicle, Computer, Laptop, Finance

# Register your models here.
admin.site.register(Vehicle)
admin.site.register(Computer)
admin.site.register(Laptop)
admin.site.register(Finance)
