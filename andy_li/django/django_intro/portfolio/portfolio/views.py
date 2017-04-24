# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
    print "-= Reached / (index.html) =-"
    return render(request, "portfolio/index.html")

def testimonials(request):
    print "-= Reached /testimonials (testimonials.html) =-"
    return render(request, "portfolio/testimonials.html")
