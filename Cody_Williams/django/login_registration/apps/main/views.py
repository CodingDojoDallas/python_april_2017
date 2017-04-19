from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def login(request):
	if request.method != 'POST':
		return redirect('/')
	else:
		if request.POST.get('email') == '' or request.POST.get('password') == '':
			messages.error(request, 'GTFO')
			return redirect('/')
		#see if the email is the db
		user = User.objects.filter(email=request.POST.get('email')).first()
		if user and bcrypt.checkpw(request.POST.get('password').encode(), user.password.encode()):
			request.session['user_id'] = user.id
			return redirect('/success')
		else:
			messages.error(request, 'GTFO')
			return redirect('/')
		#if it is verify the password

def createUser(request):
	if request.method != 'POST':
		return redirect('/')
	else:
		check = User.objects.validateUser(request.POST)
		if check[0] == False:
			for error in check[1]:
				messages.error(request, error)
			return redirect('/')
		else:
			#create the user
			hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
			user = User.objects.create(
				name = request.POST.get('name'),
				email = request.POST.get('email'),
				password = hashed_pw
			)
			request.session['user_id'] = user.id
			return redirect('/success')
			#add them to session
