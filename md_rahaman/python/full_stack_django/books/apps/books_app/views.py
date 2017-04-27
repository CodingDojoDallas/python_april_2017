from django.shortcuts import render

from .models import Books
# Create your views here.

def index(request):
	# book1 = Books.objects.create(title = 'Shutter Iland', author='soikat', published_date='2010-08-17 00:00:00', category='suspense')
	# book2 = Books.objects.create(title = 'Sutter Iland1', author='soikat', published_date='2010-08-17 00:00:00', category='suspense')
	# book3 = Books.objects.create(title = 'Shutter Iland3', author='soikat', published_date='2010-08-17 00:00:00', category='suspense')
	# book4 = Books.objects.create(title = 'Shutter Iland4', author='soikat', published_date='2010-08-17 00:00:00', category='suspense')
	# book5 = Books.objects.create(title = 'Shutter Iland5', author='soikat', published_date='2010-08-17 00:00:00', category='suspense')
	books = Books.objects.all()
	print '*'*50
	for book in books:
		print book
	print '*'*50
	
  	return render(request, 'books_app/index.html')

# '2017-08-17 00:00:00'