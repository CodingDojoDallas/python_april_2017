from django.shortcuts import render, redirect
import random

def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
	if 'activities' not in request.session:
		request.session['activities'] = []
	return render(request,'index.html')

def get_gold(request):
	print request.POST['house']
	if request.POST['house'] == 'farm':
		gold = random.randint(10, 20)
	elif request.POST['house'] == 'cave':
		gold = random.randint(5, 10)
	elif request.POST['house'] == 'house':
		gold = random.randint(2, 5)
	else:
		gold = random.randint(-50, 50)
	request.session['gold'] += gold
	if gold >0:
		action = 'Earned'
	if gold <0:
		action = 'Lost'

	message = '{} {} gold from the {}'.format(action, abs(gold), request.POST['house'])
	print message
	request.session['activities'].append(message)
	print request.session['activities']

	return redirect('/')

