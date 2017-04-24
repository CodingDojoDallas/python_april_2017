# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

def index(request):
    print "-= Reached / (index.html) =-"
    return render(request, "belt_reviewer/index.html")
