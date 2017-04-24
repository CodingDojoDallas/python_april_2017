# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Product

def index(request):
    print "-= Reached / (index.html) =-"
    product1 = Product.objects.create(name = "Nexus 6P", description = "Android phone", weight = "178", price = "500.00", cost = "250.00", category = "smartphone")
    product2 = Product.objects.create(name = "Nexus 5X", description = "Android phone", weight = "136", price = "400.00", cost = "200.00", category = "smartphone")
    product3 = Product.objects.create(name = "Nexus 6", description = "Android phone", weight = "184", price = "450.00", cost = "150.00", category = "smartphone")

    products = Product.objects.all()
    print products

    for product in products:
        print product.name

    return render(request, "products/index.html")
