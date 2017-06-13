# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
from django.db.models import Count

# helper function to get current user id
def current_user(request):
    return User.objects.get(id = request.session["user_id"])


def index(request):
    print "-= Reached / (index.html) =-"
    print request.session.items()
    return render(request, "belt_reviewer/index.html")

def createUser(request):
    print "-= Reached /users/create (redirect to books.html) =-"
    if request.method != "POST":
        return redirect("/")

    # validate user reg fields
    check = User.objects.validateUserReg(request.POST)
    if check["pass"] is False:
        for error in check["errors"]:
            messages.error(request, error)
        return redirect("/")

    # create user via create_user function
    user = User.objects.create_user(request.POST)
    print User.objects.all()
    # created user into db, add user id to session to log in
    request.session["user_id"] = user.id
    return redirect("/books")


def loginUser(request):
    print "-= Reached /login (redirect to books.html) =-"
    if request.method != "POST":
        return redirect("/")

    # validate login via validateUserLog from models.py
    check = User.objects.validateUserLog(request.POST)
    if check["pass"] is False:
        messages.error(request, check["errors"])
        return redirect("/")

    # valid email, password for login, store user id to session, go to books.html
    request.session["user_id"] = check["user"].id
    return redirect("/books")

def books(request):
    print "-= Reached /books (books.html) =-"
    # verify user is registered or logged with session user_id to reach books.html
    if "user_id" not in request.session:
        return redirect("/")
    recent_rev = Review.objects.select_related("book").all().order_by("-created_at")[:3]
    other_rev = Review.objects.select_related("book").all().order_by("-created_at")[3:]

    data = {
        "current_user": current_user(request),
        "reviews": recent_rev,
        "other_rev": other_rev,
    }
    return render(request, "belt_reviewer/books.html", data)

def logout(request):
    print "-= Reached /logout (redirect to /) =-"
    request.session.clear()
    return redirect("/")

def addBookReview(request):
    print "-= Reached /books/add (add.html) =-"
    data = {
        "authors": Author.objects.values("name").distinct(),
    }
    return render(request, "belt_reviewer/add.html", data)

def createBookReview(request):
    print "-= Reached /books/create (redirect to /books/<book_id>) =-"
    if request.method != "POST":
        return redirect("/")

    # validate author, book, reviews fields
    # checkAuth = validateAuthor(request.POST)
    # checkAuth unneeded, if author_new is blank, selection author used,
    #   else if author_new inputed, author_new value will be used instead
    #   (logic in create_author() method)
    checkBook = validateBook(request.POST)
    checkRev = validateReview(request.POST)
    if checkBook["pass"] is False or checkRev["pass"] is False:
        for error in checkBook["errors"]:
            messages.error(request, error)
        # for error in checkAuth["errors"]:
        #     messages.error(request, error)
        for error in checkRev["errors"]:
            messages.error(request, error)
        return redirect("/books/add")

    # create author
    this_author = Author.objects.create_author(request.POST)
    # create book
    this_book = Book.objects.create_book(request.POST, this_author)
    # create review
    this_review = Review.objects.create_review(request.POST, current_user(request), this_book)

    return redirect("/books/{}".format(this_book.id))


def showBook(request, book_id):
    print "-= Reached /books/<book_id> (show_book.html) =-"
    this_book = Book.objects.filter(id = book_id).first()
    this_book_reviews = this_book.reviews.all()
    data = {
        "book": this_book,
        "reviews": this_book_reviews,
        "current_user": current_user(request),
    }
    return render(request, "belt_reviewer/show_book.html", data)

def deleteBookReview(request, rev_id):
    print "-= Reached /reviews/delete/<rev_id> (redirect to /books/<book_id>) =-"
    this_review = Review.objects.filter(id = rev_id).first()
    this_book = this_review.book
    if this_review:
        this_review.delete()
    return redirect("/books/{}".format(this_book.id))

def createReview(request, book_id):
    print "-= Reached /reviews/create/<book_id> (redirect to /books/<book_id>) =-"
    this_book = Book.objects.filter(id = book_id).first()

    checkRev = validateReview(request.POST)
    if checkRev["pass"] is False:
        for error in checkRev["errors"]:
            messages.error(request, error)
    else:
        this_review = Review.objects.create_review(request.POST, current_user(request), this_book)
    return redirect("/books/{}".format(this_book.id))

def showUser(request, user_id):
    print "-= Reached /users/<user_id> (show_user.html) =-"
    this_user = User.objects.annotate(num_rev = Count("reviews")).filter(id = user_id).first()
    # user_num_rev = len(this_user.reviews.all())

    these_rev = this_user.reviews.all()
    unique_books = []
    for review in these_rev:
        if review not in unique_books:
            unique_books.append(review.book)

    data = {
        "user": this_user,
        "books": unique_books,
        # "num_rev": user_num_rev,
    }
    return render(request, "belt_reviewer/show_user.html", data)
