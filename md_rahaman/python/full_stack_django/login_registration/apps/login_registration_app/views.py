from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
# Create your views here.

def index(request):

	return render(request, "login_registration_app/index.html")

def success(request):
	print request.session['user_name']
	context = {
		"users": User.objects.all()
	}
	return render(request, "login_registration_app/success.html",context)

def createUser(request):
	if request.method != 'POST':
		return redirect('/')
	else:

		check = User.objects.validateUser(request.POST)
		if check[0] == False:
			for error in check[1]:
				print error
				messages.error(request,error)
			return redirect('/')
		else:
			hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
			user = User.objects.create(
				first_name = request.POST.get('first-name'),
				last_name = request.POST.get('last-name'),
				email = request.POST.get('email'),
				password = hashed_pw
			)
			print 'user_id: ',user.id
			# request.session['user_id'] = user.id
			request.session['user_name'] = user.first_name
			return redirect('/success')


def login(request):
	print 'login'
	if request.method != 'POST':
		return redirect('/')
	else:
		#see if the email is in the db
		#
		user = User.objects.filter(email= request.POST.get('email')).first()
		if user and bcrypt.checkpw(request.POST.get('password').encode(),user.password.encode()):
			request.session['user_name'] = user.first_name
			return redirect('/success')
		else:
			messages.error(request,'invalid')
			return redirect('/')

def logout(request):
	request.session.pop('user_name',None)
	return redirect('/')



