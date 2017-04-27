from django.shortcuts import render,redirect
import os
from random import randint
import datetime

# Create your views here.


def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
		request.session['money'] = 0
		request.session['activities'] = []
  	return render(request, 'ninja_gold_app/index.html')

def process_money(request):
	now = datetime.datetime.now()

	if request.method == 'POST':
		if request.POST['action'] == 'farm':
			rand = randint(10,20)
			request.session['money'] = rand
			request.session['gold'] = request.session['gold'] + rand

		elif request.POST['action'] == 'cave':
			rand = randint(5,10)
			request.session['money'] = rand
			request.session['gold'] = request.session['gold'] + rand

		elif request.POST['action'] == 'house':
			rand = randint(2,5)
			request.session['money'] = rand
			request.session['gold'] = request.session['gold'] + rand

		else:
			rand = randint(-50,50)
			request.session['money'] = rand
			request.session['gold'] = request.session['gold'] + rand

		if rand>0:
			action = 'Earned'
			color = 'green'

		else:
			action = 'Takes'
			color = 'red'

		message = "{} {} golds from {} {}".format(action, request.session['money'], request.POST['action'],now)
		request.session['activities'].append({'color': color, 'message':message})

		print  request.session['activities']
		return redirect('/')

	return redirect('/')
def reset(request):
	print '*'*50
	request.session.pop('gold',None)
	print '*'*50
	return redirect('/')




	# context = {
		# 	'name' : request.POST['name'],
		# 	'location' : request.POST['location'],
		# 	'favorite_language' : request.POST['favorite_language'],
		# 	'comment' : request.POST['comment'],
		# }