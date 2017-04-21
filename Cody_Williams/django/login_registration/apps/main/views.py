from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Count
from .models import *
import bcrypt
from datetime import datetime
import pytz
utc = pytz.utc

def current_user(request):
	return User.objects.get(id=request.session['user_id'])

# Create your views here.
def index(request):
	return render(request, 'main/index.html')

def login(request):
	if request.method != 'POST':
		return redirect('/')
	else:
		if request.POST.get('email') == '' or request.POST.get('password') == '':
			messages.error(request, 'invalid credentials')
			return redirect('/')
		check = User.objects.loginUser(request.POST)
		if check['status'] == False:
			messages.error(request, check['message'])
			return redirect('/')
		else:
			request.session['user_id'] = check['user'].id
			return redirect('/success')

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

def success(request):
	context = {
		'recent_posts': Post.objects.select_related('user').order_by('-created_at').all()[:5],
		'current_user': current_user(request),
		'current_datetime': datetime.now(tz=utc), 
	}
	return render(request, 'main/success.html', context)

def createPost(request):
	if request.method != 'POST':
		return redirect('/')
	else:
		check = Post.objects.validatePost(request.POST)
		if check['status'] == False:
			for error in check['errors']:
				messages.error(request, error)
		else:
			Post.objects.create(
				post=request.POST.get('post'),
				user=User.objects.get(id=request.session['user_id'])
			)
		return redirect('/success')

def likePosts(request, id):
	if request.method != 'POST':
		return redirect('/success')
	else:
		user = User.objects.get(id=request.session['user_id'])
		post = Post.objects.get(id=id)
		post.likes.add(user)
		return redirect('/success')

def showPosts(request, id):
	post = Post.objects.get(id=id)
	context = {
		'post': post,
	}
	return render(request, 'main/show_post.html', context)

def createComment(request, id):
	user = User.objects.get(id=request.session['user_id'])
	post = Post.objects.get(id=id)
	Comment.objects.create(
		comment=request.POST.get('comment'),
		user=user,
		post=post
	)
	return redirect('/posts/{}'.format(id))

def deletePost(request, id):
	if request.method != 'POST':
		return redirect('/')
	else:
		post = Post.objects.filter(id=id).first()
		if post:
			post.delete()
		return redirect('/success')

def secrets(request):
	context = {
		'posts': Post.objects.annotate(num_likes=Count('likes')).order_by('-num_likes').all(),
		'current_user': current_user(request)
	}
	return render(request, 'main/secrets.html', context)







