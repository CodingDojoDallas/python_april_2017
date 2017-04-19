# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Product

def index(request):

	product = Product.objects.create(name="Jason",description="alsekjdflsddfsf",weight=15,price=12,cost=10,category='shoes')
	print Product.laugh()
	print product
	return render(request,"products/index.html")





# Create your views here.
