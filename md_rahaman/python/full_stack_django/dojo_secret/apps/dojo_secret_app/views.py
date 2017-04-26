from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt
from datetime import datetime 
from django.db.models import Count
import pytz
utc = pytz.utc
# Create your views here.

##############funciton for userlookup##############
def current_user(request):
	return User.objects.get(id=request.session['user_id'])

def index(request):

	return render(request, "dojo_secret_app/index.html")

def success(request):
	# print request.session['user_name']
	# print request.session['user_id']
	# created_time = Secret.objects.all()[0].created_at
	# created_time_zone = created_time.astimezone(pytz.timezone('US/Central'))

	# now = datetime.datetime.now(tz=pytz.timezone('US/Central'))

	# tdelta = now - created_time_zone
	# tdelta_s = tdelta.total_seconds()/3600

	# print created_time_zone
	# print now
	# print tdelta_s

	# time = []
	# delta = []
	# ids=[]

	# for i in Secret.objects.all():

	# 	# print i.created_at
	# 	# print 'id',i.id

	# 	created_time = i.created_at
	# 	created_time_zone = created_time.astimezone(pytz.timezone('US/Central'))
	# 	now = datetime.datetime.now(tz=pytz.timezone('US/Central'))
	# 	tdelta = now - created_time_zone
	# 	tdelta_s = tdelta.total_seconds()/3660
	# 	time_format = created_time_zone.strftime('%B %d, %Y, %I %M %p')
	# 	delta.append(tdelta_s)
	# 	time.append(time_format)
	# 	ids.append(i.id)

	# dicts = dict(zip(ids,time))
	# print dicts
	# for key in dicts:
	# 	print key, dicts[key]


	# print delta
	# print time
	# print ids
	# print dicts




	context = {
		"secrets": Secret.objects.select_related('user').order_by('-created_at').all()[0:5],
		"current_user": current_user(request),
		"current_datetime":datetime.now(tz=utc)
	}

	return render(request, "dojo_secret_app/success.html",context)


def postSecrets(request):
	if request.method != 'POST':
		return redirect('/')

	else:
		#create post object
		secret = Secret.objects.create(
			secret = request.POST['secret'],
			user = User.objects.get(id=request.session['user_id'])

			)
		return redirect('/success')

def favorite(request):
	print 'favorite'
	secrets = Secret.objects.annotate(num_like = Count('likes')).all().order_by('-num_like')

	# user = User.objects.get(id=request.session['user_id'])
	for user in secrets:
		print user

	context = {
		"secrets": secrets,
		"current_user": current_user(request)
	}
	return render(request,"dojo_secret_app/favorite.html",context)

def likes(request,secretid):
	print 'likes'
	print secretid

	secret = Secret.objects.get(id=secretid)
	secret.likes.add(current_user(request))

	return redirect('/success')

def deleteSecrets(request,secretid):
	print secretid
	print 'deletepost'

	secret=Secret.objects.filter(id=secretid)
	secret.delete()

	return redirect('/success')


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
			request.session['user_id'] = user.id
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
			request.session['user_id'] = user.id
			return redirect('/success')
		else:
			messages.error(request,'invalid')
			return redirect('/')

def logout(request):
	request.session.pop('user_name',None)
	return redirect('/')



