from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# from datetime import datetime
import bcrypt
# import pytz
# utc = pytz.utc

# Create your views here.
def current_user(request):
	return User.objects.get(id = request.session['user_id'])

def index(request):
	return render(request, 'belt_app/index.html')

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
		hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
			
	#create user
	user = User.objects.create(
		first_name = request.POST.get('first_name'),
		last_name = request.POST.get('last_name'),
		email = request.POST.get('email'),
		password = hashed_pw,
	)

	#add user to session, logging them in
	request.session['user_id'] = user.id
	#route to success page
	return redirect('/books')

def login(request):
	#find user
	user = User.objects.filter(email = request.POST.get('email')).first()

	#Check user credentials
	#add them to session and log in or add error message and route to home page
	if user and bcrypt.checkpw(request.POST.get('password').encode(), user.password.encode()):
		request.session['user_id'] = user.id
		return redirect('/books')
	else: 
		messages.add_message(request, messages.INFO, 'invalid credentials', extra_tags="login")
		return redirect('/')
	return redirect('/books')

def success(request):
	context = {
		'user': current_user(request),
		'reviews': Review.objects.select_related('user').all().order_by('-created_at')[:3],
		'other_reviews': Review.objects.all().order_by('-created_at')[4:]
	}
	return render(request, 'belt_app/books.html', context)

def new_book(request):
	return render(request, 'belt_app/addBook.html')

def add_book(request):
	print request.method
	if request.method != 'POST':
		print 'we are here'
		return redirect('/books')
	#validate author
	if len(request.POST['add_author']) < 1:
		author_name = request.POST['select_author']
	else:
		author_name = request.POST['add_author']
	#create author
	author = Author.objects.create(
		name = author_name
		)
	#create book
	book = Book.objects.create(
		title = request.POST.get('title'),
		author = author
		)
	#create reviews
	review = Review.objects.create(
		review = request.POST.get('review'),
		rating = request.POST.get('rating'),
		user = current_user(request),
		book = book,
	)
	#redirect to book page
	return redirect('/books/{}'.format(book.id))

def add_review(request, id):
	book = Book.objects.get(id = id)
	#create reviews
	review = Review.objects.create(
		review = request.POST.get('review'),
		rating = request.POST.get('rating'),
		user = current_user(request),
		book = book,
	)
	return redirect('/books/{}'.format(book.id))

def show_book(request, id):
	context = {
		'current_user': current_user(request),
		'book': Book.objects.get(id = id),
		'reviews': Review.objects.filter(book = id)
	}
	return render(request, 'belt_app/show_book.html', context)

def delete_review(request, id):
	review = Review.objects.get(id=id)
	book_id = review.book.id
	review.delete()
	return redirect('/books/{}'.format(book_id))

def user(request, id):
	context = {
		'user': User.objects.get(id = id),
		'reviews': Review.objects.filter(user = id)
	}
	return render(request, 'belt_app/user.html', context)

def logout(request):
	request.session.clear()
	return redirect('/')













