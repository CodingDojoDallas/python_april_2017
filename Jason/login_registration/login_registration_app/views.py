# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from models import *
from django.contrib import messages
import bcrypt


def index(request):
	return render(request,"login_registration/index.html")

def login(request):
	if request.method != 'POST':
		return redirect('/')
	else:
		user = User.objects.filter(email=request.POST.get('email')).first()
		if request.POST.get('email') == '' or request.POST.get('password') == '':
			messages.error(request, 'GTFO')
			return redirect('/')			

		
		if user and bcrypt.checkpw(request.POST.get('password').encode(),user.password.encode()):
			request.session['user_id'] = user.id
			return redirect('/success')
		else:
			messages.error(request, 'GTFO')
			return redirect('/')


def createUser(request):
	if request.method != 'POST':
		return redirect('/')

	else:
		check = User.objects.validateUser(request.POST)
		if check[0] == False:
			for error in check[1]:
				messages.error(request,error)
			return redirect('/')
		else:
			hashed_pw = bcrypt.hashpw(request.POST.get('password'), salt)
			user = User.objects.create(
				name = request.POST.get('name'),
				email = request.POST.get('email'),
				password = hashed_pw,
			)
			request.session['user_id'] = user.id
			return redirect('/secrets')


		return redirect('/')