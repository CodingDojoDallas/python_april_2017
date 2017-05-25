from django.shortcuts import render, HttpResponse, redirect
import random


# Create your views here.
def index(request):
	print ('at index')
	del request.session['words']
	
	return render(request, 'first_app/index.html')

def process(request):
	if request.method == 'POST':
		if len(request.POST['number'])>0 and int(request.POST['number']) > 0:
		
			random_words = []

			num = int(request.POST['number'])
			list = ['one', 'two', 'three']
			
			for bleh in range(0, num):
				word = random.choice(list)
				random_words.append(word)
				
			request.session['words'] = random_words
				 
			print request.session['words']

			return redirect('/results')
		else:
			return redirect('/')
			
def results(request):
	print ('made it to show')

	return render(request, 'first_app/results.html')


		
		
