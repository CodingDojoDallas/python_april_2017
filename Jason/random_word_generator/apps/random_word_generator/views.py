# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse,redirect
import string
import random

def index(request):
	return render(request, "random_word_generator/index.html")

def wordgenerate(request):
	# increment count by 1
	print "*"*50
	if 'count' not in request.session:
		request.session['count'] = 1
	else:
		request.session['count'] += 1

	# generate 14 random alphabetical characters		
	alphabets = string.letters
	random_word=""

	for length in range(14):
		random_word += random.choice(alphabets)
	print random_word

	request.session['word'] = random_word
	print random_word
 	return redirect('/')

