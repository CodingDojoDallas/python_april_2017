# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse


def index(request):
	return render(request,"python/index.html")

def testimonials(request):
	return render(request,"python/testimonials.html")	

# Create your views here.
