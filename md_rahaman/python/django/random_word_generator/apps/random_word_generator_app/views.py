from django.shortcuts import render,redirect

# Create your views here.
from django.shortcuts import render
import uuid
import string 
from random import randint




# Create your views here.

def index(request):
	if 'attempts' not in request.session:
		request.session['attempts'] = 0	
  	return render(request, 'random_word_generator_app/index.html')

def random(request):
	print "*"*50
	str = uuid.uuid4()
	character =  string.uppercase 
	# + string.digits 
	# + string.punctuation
	# string.lowercase +
	char_len = len(character)
	# you can specify your password length here
	pass_len = 14
	password = ''
	for x in range(pass_len):
		password = password + character[randint(0,char_len-1)]
	print "*"*50
	request.session['password'] = password
	request.session['attempts'] += 1
	return redirect('/')







