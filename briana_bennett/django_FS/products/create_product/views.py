from django.shortcuts import render, redirect
from .models import Product
# Create your views here.

def index(request):

	Product.objects.create(name="truck", description="big", weight='3000', price='24.99', cost='23.00', category="vehicles")
	Product.objects.create(name="car", description="smaller", weight='2000', price='25.99', cost='24.00', category="vehicles")
	Product.objects.create(name="turtle", description="tiny", weight='50', price='4.99', cost='9.00', category="vehicles")
	product = Product.objects.all()
	print product


	return render(request, 'create_product/index.html')


	
