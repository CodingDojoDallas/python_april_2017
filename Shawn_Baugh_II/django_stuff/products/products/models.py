from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    weight = models.CharField(max_length=4)
    price = models.CharField(max_length=5)
    cost_to_seller = models.CharField(max_length=5)
    category = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
