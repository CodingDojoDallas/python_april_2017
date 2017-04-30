from django.shortcuts import render, redirect
from .models import Book
# Create your views here.

def index(request):
	print ('INDEX')
	context = {
	'books': Book.objects.all()
	}

	return render(request, 'first_app/index.html', context)

def process(request):
	print ('PROCESS')

	Book.objects.create(title=request.POST['title'], category=request.POST['category'], author=request.POST['author'])
	print Book.objects.all()

	for i in Book.objects.all():
		print i.title
		print i.author
		print i.category

	return	redirect('/')