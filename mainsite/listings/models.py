from django.db import models

class Listing(models.Model):
    item_type = models.CharField(max_length=20)
    item_color = models.CharField(max_length=10)
    item_brand = models.CharField(max_length=30)
    item_condition = models.CharField(max_length=10)
    item_material = models.CharField(max_length=20)
    item_price = models.FloatField()
    listing_date = models.DateTimeField('date listed')

    def __str__(self):
        return f"{self.item_color} {self.item_brand} {self.item_type}"
