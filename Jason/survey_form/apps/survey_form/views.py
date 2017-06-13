# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse

def index(request):
	
	if not request.session._session_key:
		request.session['times']=0
		### request.session.create()
	return render(request, "survey_form/index.html")

def survey_process(request):
	request.session['times'] += 1

	if request.method == 'POST':
			request.session['name']= request.POST["name"]
			request.session["location"]= request.POST["location"]
			request.session["language"]= request.POST["language"]
			request.session["comment"]= request.POST["comment"]
	
	print request.session['name']
	return render(request,"survey_form/result.html")



