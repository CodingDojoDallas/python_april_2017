# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# from models import Wall


def index(request):
    print "-= Reached / (index.html) =-"
    return render(request, "the_wall/index.html")
