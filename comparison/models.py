from django.db import models # type: ignore

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class DeliveryApp(models.Model):
    name = models.CharField(max_length=100)
    website_url = models.URLField()

    def __str__(self):
        return self.name


class Price(models.Model):
    food_item = models.ForeignKey(FoodItem, related_name='prices', on_delete=models.CASCADE)
    delivery_app = models.ForeignKey(DeliveryApp, related_name='prices', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    coupon_code = models.CharField(max_length=50, blank=True, null=True)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.food_item.name} - {self.delivery_app.name}"

    def save(self, *args, **kwargs):
        if self.coupon_code:
            # Apply coupon discount (This is just a placeholder logic, adjust as needed)
            self.final_price = self.price * 0.9  # 10% discount for example
        else:
            self.final_price = self.price
        super().save(*args, **kwargs)
