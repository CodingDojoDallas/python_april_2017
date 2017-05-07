from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.

def index(request):
	print ('whats up')

	if 'attempts' not in request.session:
		request.session['attempts'] = 0
		request.session['randomword'] = ""
	print request.session['attempts']

	return render(request, 'first_app/index.html')

def randomWord(request):
	if request.method == 'POST':
		print ('we made it to randomWord')
		words = ["awesome", 'changeling', 'santa','hooker','boobs','titan','Timber']

		
		request.session['randomword'] = random.choice(words)
		request.session['attempts'] = request.session['attempts'] + 1
		print request.session['randomword']

		return redirect('/')
	else:
		return redirect('/')

def popAttempts(request):
	if request.method == "POST":

		del request.session['attempts']
		del request.session['randomword']

		return redirect('/')
	else:
		return redirect('/')


