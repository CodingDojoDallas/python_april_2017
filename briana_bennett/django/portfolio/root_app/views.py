from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'root_app/index.html')

def testimonials(request):
	return render(request, 'root_app/testimonials.html')