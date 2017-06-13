# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import requires_csrf_token
import random

def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0

	if 'activities' not in request.session:
		request.session['activities'] = []
	print request.session['gold']
	return render(request,"ninja_gold/index.html")

def process_money(request, location):
	print location
	if request.POST['location'] == 'farm':
		gold = random.randint(1,20)

	elif request.POST['location'] == 'cave':
		gold = random.randint(5,10)

	elif request.POST['location'] == 'house':
		gold = random.randint(2,5)

	else: 
		gold = random.randint(-50,50)

	request.session['gold'] += gold

	messageObj = {}

	if gold > 0:
		action = "Earned"
		messageObj['color'] = 'green'

	else:
		action = "Lost"
		messageObj['color'] = 'red'

	### message with two attributes
	message = "{} {} gold from the {}".format(action, abs(gold), request.POST['location'])
	messageObj['message'] = message
	request.session['activities'].insert(0,messageObj)
	return redirect('/')

# Create your views here.
