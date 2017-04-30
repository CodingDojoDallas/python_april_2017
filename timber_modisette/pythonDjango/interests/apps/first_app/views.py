from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt
import datetime
import pytz 
from django.db.models import Count


utc = pytz.utc
def current_user(request):
	return User.objects.get(id=request.session['user_id'])


def index(request):
	print('index')



	return render(request, 'first_app/index.html')


def processUserAndInterest(request):
	print('processUserAndInterest')
	if request.method != "POST":
		return redirect('/')
	else:

		check = User.objects.validateUser(request.POST)
		if check[0] == False:
			for errors in check[1]:
				messages.error(request, errors)

			return redirect('/')

		else:
			#checking database to see if user and interest already exist
			user = User.objects.filter(name=request.POST['name']).first()
			interest = Interest.objects.filter(content=request.POST['interest']).first()

			if interest is None and user is None:
				print "hello"
				request.session['user_id']= user.id

				create_user = User.objects.create(name=request.POST.get('name'))
				interest = Interest.objects.create(content=request.POST.get('interest'))
				user = create_user.interests.add(interest)
				return redirect('/show')
				#if interest does not exist create interest and add existing user
			if user != None:
				user = User.objects.filter(name=request.POST['name']).first()
				interest = Interest.objects.create(content=request.POST['interest'])
				user.interests.add(interest)
				request.session['user_id']= user.id
				return redirect('/show')

		 		#if user doesnt exist create user and add existing interest
			if interest != None:
				user = User.objects.create(name=request.POST['name'])
				interest = Interest.objects.filter(content=request.POST['interest'])
				request.session['user_id']= user.id
				return redirect('/show')
			





	
			







			return redirect('/show')
			
			
def show(request):
	print('show')

	context = {'users': User.objects.all(), 'interest':Interest.objects.all(), 'current_user':current_user(request)}

	return render(request, 'first_app/show.html', context)

def userProfile(request, userid):
	print('userProfile')

	user = User.objects.get(id=userid)
	emptyList =[]

	for i in user.interests.all():
		if i.content not in emptyList:
			emptyList.append(i.content)

	print emptyList

	context = {'user': user, 'content':emptyList, 'current_user': current_user(request)}

	return render(request, 'first_app/users.html', context)



def delete(request, interest):
	print interest 

	interest = Interest.objects.filter(content=interest).first()
	print interest.content

	interest.delete()



	



	return redirect('/show')


			

			






