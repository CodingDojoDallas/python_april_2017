# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
	return render(request,"the_wall/index.html")
# Create your views here.
