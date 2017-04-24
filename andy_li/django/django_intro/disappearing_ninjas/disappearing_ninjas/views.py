# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
    print "-= Reached / (index.html) =-"
    return render(request, "disappearing_ninjas/index.html")

def ninjas(request, color = "tmnt_all"):
    print "-= Reached /ninjas/<color> =-"
    if color in ["blue", "orange", "red", "purple", "tmnt_all"]:
        img = color
    else:
        img = "april"

    data = {
        "img": "disappearing_ninjas/img/{}.jpg".format(img)
    }
    print data
    return render(request, "disappearing_ninjas/ninjas.html", data)
