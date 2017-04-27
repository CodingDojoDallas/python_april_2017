from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
# Create your views here.

def index(request):

	return render(request, "username_validation_app/index.html")

def process(request):
	if request.method == 'POST':
		name = User.objects.name_validation(request.POST['name'])
		if name == True:
			User.objects.create(name=request.POST['name'])
			print True
			return redirect('/success')
		else:
			message = "length should be between 9-15"
			messages.error(request,message)
			return redirect('/')

def success(request):	

	context = {
		"users":User.objects.all()
	}

	return render(request,"username_validation_app/success.html",context)
