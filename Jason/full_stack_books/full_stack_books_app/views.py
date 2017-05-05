# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import Book

def index(request):
	books=Book.objects.all()
	print Book.objects.all().count()
	return render(request,"full_stack_books/index.html",{"books":books})


def add(request):
	if request.method == 'POST':
		b = Book.objects.create(title=request.POST['title'],category=request.POST['category'],author=request.POST['author'])
		print b	

	books=Book.objects.all()[0]
	print Book.objects.all().count()
	print books[0]
	return render(request,"full_stack_books/index.html",context)			



