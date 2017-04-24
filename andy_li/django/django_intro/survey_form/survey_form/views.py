# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

def index(request):
    print "-= Reached / (index.html) =-"
    if "submit_num" not in request.session:
        request.session["submit_num"] = 0

    return render(request, "survey_form/index.html")

def result(request):
    print "-= Reached /result (result.html) =-"
    return render(request, "survey_form/result.html")

def process(request):
    print "-= Reached /surveys/process (redirects to /result) =-"
    request.session["submit_num"] += 1
    data = {
        "name" : request.POST["name"],
        "loc_select" : request.POST["loc_select"],
        "fav_lang" : request.POST["fav_lang"],
        "comment" : request.POST["comment"],
    }
    request.session["user"] = data

    print data
    return redirect("/result")
