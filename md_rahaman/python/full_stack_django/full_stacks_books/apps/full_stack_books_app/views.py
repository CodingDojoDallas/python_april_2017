from django.shortcuts import render,redirect
from .models import Book

# Create your views here.



def index(request):

	context = {
		"books":Book.objects.all()
	}

	return render(request, "full_stack_books_app/index.html",context)

def add(request):
	title = request.POST['title']
	category = request.POST['category']
	author = request.POST['author']

	Book.objects.create(title=request.POST['title'], author=request.POST['author'], category=request.POST['category'])

	print '*'*50
	print 'title =',title
	print 'category =',category
	print 'author =',author
	print '*'*50


	return redirect('/')

