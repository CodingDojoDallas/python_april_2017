from django.shortcuts import render, HttpResponse

def index(request):
	return render(request, 'first_app/index.html')

def show(request):
	print request.method
	return render(request, 'first_app/showusers.html')
