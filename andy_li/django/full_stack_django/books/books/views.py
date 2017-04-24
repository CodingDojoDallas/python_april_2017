# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from models import Book

def index(request):
    print "-= Reached / (index.html) =-"

    book1 = Book.objects.create(title = "Milk and Honey", author = "Rupi Kaur", pub_date = "2015-10-06", category = "American Poetry")
    book2 = Book.objects.create(title = "Happy Book 1", author = "Happy Gilmore", pub_date = "1903-10-01", category = "Comedy")
    book3 = Book.objects.create(title = "Happy Book 2", author = "Happy Gilmore", pub_date = "1903-10-02", category = "Tragedy")
    book4 = Book.objects.create(title = "Happy Book 3", author = "Happy Gilmore", pub_date = "1903-10-03", category = "Sci-Fi")
    book5 = Book.objects.create(title = "Happy Book 4", author = "Happy Gilmore", pub_date = "1903-10-04", category = "Romance")

    books = Book.objects.all()
    for book in books:
        print book

    return render(request, "books/index.html")
