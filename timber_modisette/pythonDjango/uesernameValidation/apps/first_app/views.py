from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
	print ('INDEX')

	return render(request, 'first_app/index.html')

def process(request):
	print ('PROCESS')
	if request.method != 'POST':
		return redirect('/')

	else:
		valid = User.objects.validateUser(request.POST)
		if valid[0] == False:
			for error in valid[1]:
				messages.error(request, error)
			return redirect('/')
		else:
			# user = User.objects.create(username=request.POST['username'])
			return	redirect('/success')

def success(request):
	print ('SUCCESS')
	user = User.objects.all()

	context = {
	'username':user
	}
	print context
	return render(request, 'first_app/success.html',context)

def remove(request, id):
	print ('REMOVE')

	deleteUser = User.objects.get(id=id)
	deleteUser.delete()

	print User.objects.all()
	
	return redirect('/')