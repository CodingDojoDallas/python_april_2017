from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
import bcrypt
from datetime import datetime
import pytz 
from django.db.models import Count


utc = pytz.utc 

# Create your views here.
def current_user(request):
	return User.objects.get(id=request.session['user_id'])


def index(request):
	print ('INDEX')

	return render(request, 'dojo_secrets/index.html')

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
			
	return redirect('/secrets')


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
			

			return redirect('/secrets')
		else:
			messages.error(request, "no")
			return redirect('/')


def secrets(request):
	print('SECRETS')
	if 'name' not in request.session:
		return redirect('/')
	if 'user_id' not in request.session:
		return redirect('/')

	else:
		username = request.session['name']
		userid = request.session['user_id']

		context = {'secrets': Post.objects.select_related('user').order_by('-created_at').all()[0:5], 'current_user': current_user(request), 'current_datetime': datetime.now(tz=utc)}
		

		

		# for i in time:
		# 	print i.created_at.strftime('%Y-%m-%d %H:%M')

		# time2 = time[0].created_at.strftime('%Y-%m-%d %H:%M') 
		

		

		return render(request, 'dojo_secrets/secrets.html', context)





def postsecrets(request):
	if request.method != 'POST':
		return redirect('/')
	else:

		
		secrets = Post.objects.create(content=request.POST['secret'], user= User.objects.get(id=request.session['user_id']))

		return redirect('/secrets')

def like(request, postid):
	print("like")

	secret = Post.objects.get(id=postid)
	user = secret.likes.add(current_user(request))

	return redirect('/secrets')



def favourites(request):
	print('FAVS')
	if 'user_id' not in request.session:
		return redirect ('/')
	if 'name' not in request.session:
		return redirect('/')

	else:
		users = User.objects.get(id=request.session['user_id'])
		secrets = Post.objects.annotate(num_like=Count('likes')).all().order_by('-num_like')

		context = {'secrets': secrets, 'current_user': current_user(request)}




		# for secret in secrets:
		# 	print secret.likes

		# for user in users:
		# 	print user.first_name
		# 	print user.liked_posts.all() #a list of post objects user has liked
		# 	for i in user.liked_posts.all():
		# 		print i.likes#printing conent of the liked posts of user

		return render(request, 'dojo_secrets/favourites.html',context)



def deletesecrets(request, postid):
	print("delete secret")

	secret = Post.objects.filter(id=postid)
	secret.delete()

	return redirect('/secrets')


def likeonFavs(request, postid):
	print("like")

	secret = Post.objects.get(id=postid)
	user = secret.likes.add(current_user(request))

	return redirect('/favourites')


def logout(request):
	print ('LOGOUT')
	request.session.delete()

	return redirect('/')
