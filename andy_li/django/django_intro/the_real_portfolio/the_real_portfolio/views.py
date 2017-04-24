# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

def index(request):
    print "-= Reached / (index.html) =-"
    return render(request, "the_real_portfolio/index.html")

def about(request):
    print "-= Reached /about (about.html) =-"
    return render(request, "the_real_portfolio/about.html")

def projects(request):
    print "-= Reached /projects (projects.html) =-"
    return render(request, "the_real_portfolio/projects.html")

def testimonials(request):
    print "-= Reached /testimonials (testimonials.html) =-"
    return render(request, "the_real_portfolio/testimonials.html")
