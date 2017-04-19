from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'root_app/index.html')

def projects(request):
	return render(request, 'root_app/projects.html')

def about_me(request):
	return render(request, 'root_app/about_me.html')

def testimonials(request):
	return render(request, 'root_app/testimonials.html')