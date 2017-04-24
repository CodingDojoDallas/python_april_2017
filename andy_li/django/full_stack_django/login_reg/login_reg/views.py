# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *


def index(request):
    print "-= Reached / (index.html) =-"
    return render(request, "login_reg/index.html")

def create(request):
    print "-= Reached /create (redirect to success.html) =-"
    if request.method != "POST":
        return redirect("/")

    # validate user reg fields
    check = User.objects.validateUserReg(request.POST)
    if check["pass"] is False:
        for error in check["errors"]:
            messages.error(request, error)
        return redirect("/")

    # create user
    hashed_pwd = bcrypt.hashpw(request.POST["password"].encode(), bcrypt.gensalt())
    user = User.objects.create(
        first_name = request.POST["first_name"],
        last_name = request.POST["last_name"],
        email = request.POST["email"],
        password = hashed_pwd,
    )
    print User.objects.all()
    # created user into db, add user id to session to log in
    request.session["user_id"] = user.id
    print request.session.items()
    return redirect("/success")


def login(request):
    print "-= Reached /login (redirect to success.html) =-"
    if request.method != "POST":
        return redirect("/")
    # verify if email, password is blank
    if len(request.POST["email"]) < 1 or len(request.POST["password"]) < 1:
        messages.error(request, "Invalid login credentials.")
        return redirect("/")

    # validate login via validateUserLog from models.py
    check = User.objects.validateUserLog(request.POST)
    if check["pass"] is False:
        messages.error(request, check["errors"])
        return redirect("/")

    # valid email, password for login, store user id to session, go to success.html
    request.session["user_id"] = check["user"].id
    print request.session.items()
    return redirect("/success")


def success(request):
    print "-= Reached /success (success.html) =-"
    data = {
        "current_user": User.objects.get(id = request.session["user_id"])
    }

    return render(request, "login_reg/success.html", data)


def logout(request):
    print "-= Reached /logout (redirect to /) =-"
    request.session.clear()
    return redirect("/")
