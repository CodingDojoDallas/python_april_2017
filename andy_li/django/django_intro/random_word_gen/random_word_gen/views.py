# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
import random, string

def index(request):
    print "-= Reached / (index.html) =-"
    if "attempt_num" not in request.session or "random_str" not in request.session:
        request.session["attempt_num"] = 0
        request.session["random_str"] = "Your random string..."

    data = {
        "attempt_num": request.session["attempt_num"],
        "random_str": request.session["random_str"],
    }

    print data
    return render(request, "random_word_gen/index.html", data)

def gen(request):
    print "-= Reached /gen (redirect back to /) =-"
    random_str = "".join([random.choice(string.ascii_letters + string.digits) for char in range(20)])
    request.session["attempt_num"] += 1
    request.session["random_str"] = random_str

    return redirect("/")

def reset(request):
    print "-= Reached /reset (redirect back to /) =-"
    request.session.clear()
    return redirect("/")
