# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
import random, string


#assign length word and list
length_of_list = random.randint(1,12)
print length_of_list
length_of_word = random.choice(range(10))
print length_of_word

#generate random word and populate the list
alphabets = string.letters
random_word_list = [] 
for list_length in range(length_of_list):
	
	random_word=""

	for word_lenght in range(length_of_word):
		random_word += random.choice(alphabets)
	
	random_word_list.append(random_word)
print random_word_list
	    


def index(request):
	return render(request,"surprise_me/index.html")


def results(request):
	if request.method == "POST":
		number=request.POST["number"]
		number=int(number)
		result_words_list = random.sample(random_word_list,number)
		context={'words':result_words_list}
		return render(request, "surprise_me/results.html",context)
	else:
		return redirect('/')

# Create your views here.
