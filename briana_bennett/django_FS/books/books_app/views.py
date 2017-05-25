from django.shortcuts import render, redirect
from .models import Book

def index(request):
	# Book.objects.create(title = 'my life', author = 'me', published_date = '2017-04-18', category = 'tragedy')
	# Book.objects.create(title = 'your life', author = 'you', published_date = '2017-05-18', category = 'comedy')
	# Book.objects.create(title = 'his life', author = 'him', published_date = '2017-06-18', category = 'drama')
	# Book.objects.create(title = 'her life', author = 'her', published_date = '2017-07-18', category = 'sci-fi')
	# Book.objects.create(title = 'their life', author = 'them', published_date = '2017-08-18', category = 'romance')
	
	books = Book.objects.all()
	print books

	return render(request, 'books_app/index.html')