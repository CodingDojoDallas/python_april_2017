from django.shortcuts import render, HttpResponse
from .models import Book
# Create your views here.
def index(request):
	print ('index')

	# book1 = Book.objects.create(title='the alchemist', author='unknown', published_date='1990-11-23 00:00:00', category='mind opening')
	
	# book2 = Book.objects.create(title='the little prince', author='unknown', published_date='1990-11-23 00:00:00', category='mind opening')

	# book3 = Book.objects.create(title='the thief lord', author='unknown', published_date='1990-11-23 00:00:00', category='mind opening')

	# book4 = Book.objects.create(title='the tao of pooh', author='unknown', published_date='1990-11-23 00:00:00', category='mind opening')

	# book5 = Book.objects.create(title='the cat in the hat', author='unknown', published_date='1990-11-23 00:00:00', category='mind opening')
	
	Book.objects.all()

	# for i in Book.objects.all():
	# 	print i

	# books = Book.object.all()

	# for i in books:
	# 	print i

	print Book.objects.all()[0]

	print Book.objects.all()[0].title


	

	return render(request, 'first_app/index.html')