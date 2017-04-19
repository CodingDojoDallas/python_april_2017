# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Book

def index(request):
	if request.method == 'GET':
		items =	[{
					'title':'abc',
					'author':'db',
					'published_date':'2017-01-02 00:00:00',
					'category':'abc',
			 	 },
			 	 {
					'title':'abc',
					'author':'db',
					'published_date':'2017-01-02 00:00:00',
					'category':'abc',
			 	 },
			 	 {
					'title':'abc',
					'author':'db',
					'published_date':'2017-01-02 00:00:00',
					'category':'abc',
			 	 },
			 	 {
					'title':'abc',
					'author':'db',
					'published_date':'2017-01-02 00:00:00',
					'category':'abc',
			 	 },
			 	 {
					'title':'abc',
					'author':'db',
					'published_date':'2017-01-02 00:00:00',
					'category':'abc',
			 	 },
			 	]

		for item in items:
			print 'item', item['title']
			Book.objects.create(title=item['title'],author=item['author'],published_date=item['published_date'],category=item['category'], inprint=True)



	print Book.objects.all()[0].title
		
	return render(request,"books/index.html")
# Create your views here.
