# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(max_length = 1000)
    weight = models.DecimalField(max_digits = 255, decimal_places = 3)
    price = models.DecimalField(max_digits = 255, decimal_places = 2)
    cost = models.DecimalField(max_digits = 255, decimal_places = 2)
    category = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
