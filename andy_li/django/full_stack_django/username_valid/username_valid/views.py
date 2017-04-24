# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *

def index(request):
    print "-= Reached / (index.html) =-"
    return render(request, "username_valid/index.html")

def create(request):
    print User.objects.all()
    # request method data is not post, redirect to index.html
    if request.method != "POST":
        return redirect("/")
    # request method data is post
    else:
        # check if post data passes validate method from models.py
        check = User.objects.validate(request.POST)
        # if validation fails, generate flash error msgs, redirect to index.html
        if check[0] == False:
            for error in check[1]:
                messages.error(request, error)
                print error
            return redirect("/")
        # validation passes, create user into db and render onto success.html
        else:
            user = User.objects.create(
                name = request.POST["username"],
            )

            return redirect("/success")

def delete(request, id):
    User.objects.get(id = id).delete()
    return redirect("/success")

def success(request):
    print "-= Reached /success (success.html) =-"
    users = User.objects.all()
    data = {
        "users": users,
        "last_user": users.last(),
    }

    return render(request, "username_valid/success.html", data)
