from django.shortcuts import render, redirect
from .models import User, Post
from django.contrib import messages
from datetime import datetime
import bcrypt
import pytz
utc = pytz.utc

# Create your views here.
def current_user(request):
	return User.objects.get(id = request.session['user_id'])

def index(request):
	return render(request, 'secret_app/index.html')

def register(request):
	check = User.objects.validateUser(request.POST)
	if request.method != 'POST':
		return redirect('/')
	if check[0] == False:
		for error in check[1]:
			messages.add_message(request, messages.INFO, error, extra_tags="registration")
			return redirect('/')
	if check[0] == True:
		#has password
		#create user
		#add user to session, logging them in
		#route to success page
		hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
			
	user = User.objects.create(
		first_name = request.POST.get('first_name'),
		last_name = request.POST.get('last_name'),
		email = request.POST.get('email'),
		password = hashed_pw,
	)

	request.session['user_id'] = user.id
	#print user
	return redirect('/success')

def login(request):
	#find user
	user = User.objects.filter(email = request.POST.get('email')).first()

	#Check user credentials
	#add them to session and log in or add error message and route to home page
	if user and bcrypt.checkpw(request.POST.get('password').encode(), user.password.encode()):
		request.session['user_id'] = user.id
		return redirect('/success')
	else: 
		messages.add_message(request, messages.INFO, 'invalid credentials', extra_tags="login")
		return redirect('/')

def success(request):
	context = {
		'user': current_user(request),
		'posts': Post.objects.select_related('user').all().order_by('-created_at')[:5],
		'current_datetime' : datetime.now(tz=utc),
	}
	return render(request, 'secret_app/secrets.html', context)

def create_post(request):
	if request.method != 'POST':
		redirect('/')
	else: 
		Post.objects.create(
			content = request.POST.get('content'),
			user = current_user(request),
			created_at = request.POST.get('created_at'),
			)
		return redirect('/success')

def popular_posts(request):
	context = {
		'user': current_user(request),
		'posts': Post.objects.select_related('user').all().order_by('likes')[:5],
		'current_datetime' : datetime.now(tz=utc),
	}
	return render(request, 'secret_app/popular_secrets.html', context)

def delete_post(request, id):
	if request.method != 'POST':
		return redirect('/')
	else: 
		post = Post.objects.filter(id=id).first()
		if post:
			post.delete()
		return redirect('/success')

def like_post(request, id):
	if request.method != 'POST':
		return redirect('/success')
	else: 
		#find this user
		user = current_user(request)
		#find this post
		post = Post.objects.get(id=id)
		# Add likes
		post.likes.add(user)
		
	return redirect('/success')

