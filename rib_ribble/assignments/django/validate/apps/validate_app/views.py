from django.shortcuts import render, redirect

# Use to import messages
from django.contrib import messages

from models import User

def index(request):
	return render(request, "validate_app/index.html")

def input(request):
	is_validated = User.objects.validate(request.POST['username'])

	if is_validated:
		User.objects.create(user_name=request.POST['username'])
		messages.success(request,"The username you entered " + request.POST['username'] + " is valid.  Thank You!")
		return redirect('/success')

	else:
		messages.error(request, "Username is not Valid!")
		return redirect('/')

	

def success(request):
	users = User.objects.all()
	context = {
		"users": users
	}
	return render(request, "validate_app/success.html", context)


