from django.shortcuts import render
from .models import Products


# Create your views here.

def index(request):

	# product = Products.objects.create(name = 'Honda', description = 'yellow', weight = 2000, price= 1.00, cost=1.50, catagory='Car')
	products = Products.objects.all()
	print '*'*50

	# print products
	for i in products:
		print i
	print '*'*50
	
  	return render(request, 'products_app/index.html')

