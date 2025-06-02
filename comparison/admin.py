from django.contrib import admin # type: ignore
from .models import FoodItem, Price

admin.site.register(FoodItem)
admin.site.register(Price)
