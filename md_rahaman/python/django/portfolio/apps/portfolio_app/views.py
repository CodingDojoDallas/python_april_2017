from django.shortcuts import render

# Create your views here.

def index(request):
	# print '*'*5+"hello_world"+'*'*5
  	return render(request, 'portfolio_app/index.html')

def testimonials(request):
	print 'testimonials'
	return render(request, 'portfolio_app/testimonials.html')