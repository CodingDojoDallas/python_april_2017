from django.shortcuts import render,redirect
import datetime
import random

# Create your views here.

VALUES = ['one','Two','Three','Four','Five','Six']

def index(request):
  	return render(request, 'surprise_me_app/index.html')

def process(request):
	if request.method == 'POST':
		# print len(request.POST['number'])
		if int(request.POST['number'])>0 and  len(request.POST['number']) > 0:
			num = int(request.POST['number'])
			request.session["num"] = num
			return redirect('/results')

	return redirect('/')

def results(request):
	# print VALUES
	# context = {}
	random.shuffle(VALUES)
	num = request.session["num"]

	context = {
		'words': VALUES[0: num]
	}
	
  	return render(request, 'surprise_me_app/results.html', context)

