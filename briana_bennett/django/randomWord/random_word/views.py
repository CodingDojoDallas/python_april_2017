from django.shortcuts import render, redirect
import random
import string

# Create your views here.
def index(request):
	return render(request, 'random_word/index.html')

def create(request):
	random_string = ''
	while(len(random_string) < 14):
		random_string += random.choice(string.ascii_lowercase)
	print random_string
	request.session['random_word'] = random_string

	if('count' not in request.session):
		request.session['count'] = 0
	else:
		request.session['count'] += 1

	
	
	return redirect('/')