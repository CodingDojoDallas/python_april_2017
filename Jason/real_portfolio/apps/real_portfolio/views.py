# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse


def index(request):
	return render(request,"real_portfolio/index.html")

def projects(request):
	return render(request,"real_portfolio/projects.html")

def about(request):
	return render(request,"real_portfolio/about.html")

def testimonials(request):
	return render(request,"real_portfolio/testimonials.html")


