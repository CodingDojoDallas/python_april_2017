from django.shortcuts import render

# Create your views here.


def index(request):
  	return render(request, 'real_portfolio_app/index.html')

def projects(request):
	return render(request, 'real_portfolio_app/projects.html')

def about(request):

	return render(request, 'real_portfolio_app/about.html')

def testimonials(request):
	return render(request, 'real_portfolio_app/testimonials.html')