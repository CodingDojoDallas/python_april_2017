# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import Course

def index(request):
    print "-= Reached / (index.html) =-"
    data = {
        "courses": Course.objects.all(),
    }

    return render(request, "courses/index.html", data)

def create(request):
    print "-= Reached /create (redirect to /) =-"
    user = Course.objects.create(
        name = request.POST["name"],
        desc = request.POST["desc"],
    )

    print user
    return redirect("/")

def confirm(request, id):
    print "-= Reached /courses/destroy/<user id> (confirm.html) =-"
    data = {
        "course": Course.objects.get(id = id),
    }

    return render(request, "courses/confirm.html", data)

def destroy(request, id):
    print "-= Reached /delete (redirect to /) =-"
    Course.objects.get(id = id).delete()

    return redirect("/")
