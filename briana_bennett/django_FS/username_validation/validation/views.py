from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
	return render(request, 'validation/index.html')

def createUser(request):
	if request.method != 'POST':
		return redirect('/')
	else: 
		check_validity = User.objects.validateUser(request.POST)
		if check_validity[0] == False:
			for error in check_validity[1]:
				messages.error(request, error)
				return redirect('/')
		if check_validity[0] == True:
			#create the user
			user = User.objects.create(
				username = request.POST.get('username')
				)
			print user

		context = {
			'user': user,
			'users': User.objects.all(),
		}




	return render(request, 'validation/success.html', context)