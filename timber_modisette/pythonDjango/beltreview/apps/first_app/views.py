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
			
	return redirect('/homepage')



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
			

			return redirect('/homepage')
		else:
			messages.error(request, "no")
			return redirect('/')



def homepage(request):
	if 'user_id' not in request.session:
		return redirect('/')
	else:
		review = Review.objects.all()

		context={'review': Review.objects.order_by('-created_at').all()[0:3], 'current_user':current_user(request)}

		return render(request, 'first_app/homepage.html', context)




def addbook(request):
	if 'user_id' not in request.session:
		return redirect('/')
	else:



		return render(request, 'first_app/addbook.html')


def book(request, bookid):
	print('book')
	if 'user_id' not in request.session:
		return redirect('/')
	else:
		book = Book.objects.filter(id=bookid)
		

		context = {'book': book, 'current_user':current_user(request)}



		return render(request, "first_app/book.html", context)



def createbook(request):
	print ('createbook')
	if request.method != "POST":
		return redirect('/')
	else:

		check = Review.objects.formValidation(request.POST)
		print check

		if check[0] == False:
			for errors in check[1]:
				messages.error(request, errors)
			return	redirect('/addbook')

		else:
			rating = int(request.POST['rating'])
	
			author = Author.objects.create(name=request.POST['authorname'])
			book = Book.objects.create(title=request.POST['book_title'], author=author, )
			review = Review.objects.create(user=current_user(request), book=book, content=request.POST['review'], rating=rating)

	

		return redirect('/book/{}'.format(book.id))


def addbookreview(request,bookid):
	if request.method != 'POST':
		return redirect('/')
	else:
		rating = int(request.POST['book_rating'])
		book= Book.objects.filter(id=bookid)[0]
		print book
		review = Review.objects.create(user=current_user(request), book=book, content=request.POST['book_review'], rating=rating)

		return redirect('/book/{}'.format(bookid))


def deletereview(request, reviewid):
	print('deletereview')
	if 'user_id' not in request.session:
		return redirect('/')
	else:
		review = Review.objects.filter(id=reviewid)
		
		review.delete()

		for i in review:
			print i.book
			print i.book.title
			print i.user.first_name

	return redirect('/homepage')

def deletebookreview(request, reviewid):
	if 'user_id' not in request.session:
		return redirect('/')
	else:
		review = Review.objects.get(id=reviewid)
		print review
		bookid = review.book.id
		print bookid
		review.delete()


	return redirect('/book/{}'.format(bookid))



def userprofile(request, userid):
	print('userprofile')
	bookarr = []
	user = User.objects.get(id=userid)

	for review in user.reviews.all():
		if review.book not in bookarr:
			bookarr.append(review.book)


	context = {'user': user, 'current_user':current_user(request), 'reviews':bookarr}



	return render(request, 'first_app/userprofile.html',context)

def logout(request):
	print ('logout')

	request.session.delete()
	return redirect('/')

# def addreview(request, bookid):
# 	print('this')
# 	book = Book.objects.filter(id=bookid)
# 	# new_review = Review.objects.create(user=current_user(request), book=book, content=request.POST['book_review'] )

# 	return redirect('book/bookid')








	
			












