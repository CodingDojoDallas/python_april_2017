# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import Book

def index(request):
    print "-= Reached / (index.html) =-"
    data = {
        "books": Book.objects.all(),
    }

    print data
    return render(request, "full_stack_books/index.html", data)

def create(request):
    print "-= Reached /create (redirect to /) =-"
    user = Book.objects.create(
        title = request.POST["title"],
        author = request.POST["author"],
        category = request.POST["category"],
    )

    print user
    return redirect("/")
