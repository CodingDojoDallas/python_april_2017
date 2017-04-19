# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.template import Template, Context
import re

def index(request):
	html = "<html><body>No ninjas here.</body></html>"
	return HttpResponse(html)

def display_all(request):
	html="<html><body><img src='/static/disappearing_ninjas/img/tmnt.png'></body></html>"
	return HttpResponse(html)

def display_color(request,color):
	color = str(color)
	print color
	if color == 'blue':
		html = "<html><body><img src='/static/disappearing_ninjas/img/leonardo.jpg'></body></html>"

	elif color == 'orange':
		html = "<html><body><img src='/static/disappearing_ninjas/img/michelangelo.jpg'></body></html>"

	elif color == 'red':
		html = "<html><body><img src='/static/disappearing_ninjas/img/raphael.jpg'></body></html>"

	elif color == 'purple':
		html = "<html><body><img src='/static/disappearing_ninjas/img/donatello.jpg'></body></html>"

	else:
		html = "<html><body><img src='/static/disappearing_ninjas/img/notapril.jpg'></body></html>"
	return HttpResponse(html)

# Create your views here.
