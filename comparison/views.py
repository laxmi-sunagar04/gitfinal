from django.shortcuts import render # type: ignore
from .models import FoodItem, Price

def compare_prices(request):
    food_items = FoodItem.objects.all()
    price_comparisons = []
    
    for food_item in food_items:
        prices = Price.objects.filter(food_item=food_item)
        price_comparisons.append({
            'food_item': food_item,
            'prices': prices,
        })

    return render(request, 'comparison/compare_prices.html', {'price_comparisons': price_comparisons})
