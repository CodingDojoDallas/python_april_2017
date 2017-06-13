# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from models import *
from django.db.models import Count

def current_user(request):
    return User.objects.get(id = request.session["user_id"])


def index(request):
    print "-= Reached / (index.html) =-"
    return render(request, "dojo_secrets/index.html")

def createUser(request):
    print "-= Reached /users (redirect to secrets.html) =-"
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
    return redirect("/secrets")


def loginUser(request):
    print "-= Reached /login (redirect to secrets.html) =-"
    if request.method != "POST":
        return redirect("/")

    # validate login via validateUserLog from models.py
    check = User.objects.validateUserLog(request.POST)
    if check["pass"] is False:
        messages.error(request, check["errors"])
        return redirect("/")

    # valid email, password for login, store user id to session, go to secrets.html
    request.session["user_id"] = check["user"].id
    print request.session.items()
    return redirect("/secrets")


def secrets(request):
    print "-= Reached /secrets (secrets.html) =-"
    # verify user is registered or logged with session user_id to reach secrets.html
    if "user_id" not in request.session:
        return redirect("/")

    data = {
        "current_user": current_user(request),
        "posts": Post.objects.select_related("user").all().order_by("-created_at")[:5],
        "liked_post_ids": User.objects.likedPost_ids(current_user(request)),
    }

    return render(request, "dojo_secrets/secrets.html", data)


def logout(request):
    print "-= Reached /logout (redirect to /) =-"
    request.session.clear()
    return redirect("/")


def createPost(request):
    print "-= Reached /posts (redirect to secrets.html) =-"
    if request.method != "POST":
        return redirect("/")

    check = Post.objects.validatePost(request.POST)
    if check["pass"] is False:
        messages.error(request, check["errors"])
    else:
        post = Post.objects.create(
            post = request.POST["post"],
            user = current_user(request),
        )
    return redirect("/secrets")

def popular(request):
    print "-= Reached /secrets/popular (popular.html) =-"
    data = {
        "current_user": current_user(request),
        "posts": Post.objects.select_related("user").all().annotate(num_likes = Count("likes")).order_by("-num_likes")
    }

    return render(request, "dojo_secrets/popular.html", data)

def likePosts(request, post_id):
    print "-= Reached /posts/likes/<post_id> (redirect to secrets.html) =-"
    # increment likes for post by user
    user = current_user(request)
    post = Post.objects.get(id = post_id)
    post.likes.add(user)

    return redirect("/secrets")

def deletePosts(request, post_id):
    print "-= Reached /posts/delete/<post_id> (redirect to secrets.html) =-"
    # delete post with specific post_id
    post = Post.objects.get(id = post_id)
    post.delete()

    return redirect("/secrets")
