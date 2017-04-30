from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
import bcrypt
from .models import *

# Create your views here.
def index(request):
	print ('INDEX')

	return render(request, 'first_app/index.html')

def register(request):
	print ('REGISTER')
	if request.method != 'POST':
		return redirect('/')
	else:
		check = User.objects.validateUser(request.POST)
		if check[0] == False:
			for errors in check[1]:
				messages.error(request, errors)

			return redirect('/')
		else:
			hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
			user = User.objects.create(first_name=request.POST.get('first_name'), last_name=request.POST.get('last_name'), email=request.POST.get('email'), password=hashed_pw )
			request.session['user_id'] = user.id
			request.session['name'] =user.first_name
			
	return redirect('/success')


def login(request):
	print ('LOGIN')
	if request.method != 'POST':
		return redirect('/')
	else:
		if request.POST.get('email') == '' or request.POST.get('password') == '':
			messages.error(request, "no")
			return redirect('/')

		user = User.objects.filter(email=request.POST.get('email')).first()
		if user and bcrypt.checkpw(request.POST.get('password').encode(),user.password.encode()):
			request.session['user_id']= user.id
			request.session['name']= user.first_name
			

			return redirect('/success')
		else:
			messages.error(request, "no")
			return redirect('/')





def success(request):
	print('SUCCESS')
	if 'name' not in request.session:
		return redirect('/')
	if 'user_id' not in request.session:
		return redirect('/')

	else:
		username = request.session['name']
		userid = request.session['user_id']
		print username
		print userid
		context = {'username': username, 'userid':userid }
		print context
	
		return render(request, 'first_app/success.html', context)


def logout(request):
	print ('LOGOUT')
	request.session.delete()

	return redirect('/')



def sendEmail(request):
	print ('sendEmail')

	send_email(subject=request.POST['subject'], message=request.POST['message'], from_email=request.POST['from'], to_list=request.POST['to'], fail_silently=True)

	return redirect('/success')

