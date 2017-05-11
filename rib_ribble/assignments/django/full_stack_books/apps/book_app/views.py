from django.shortcuts import render, redirect
from models import Book 

def index(request):
	books = Book.objects.all()
	context = {
		"books": books
	}
	return render(request, "book_app/index.html", context)

def input(request):
	Book.objects.create(title=request.POST['title'],author=request.POST['author'],
		category=request.POST['category'])
	return redirect('/')
