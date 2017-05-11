from django.shortcuts import render, redirect
import random

def index(request):
	if not 'count' in request.session:
		request.session["count"] = 0
	if not 'activities' in request.session:
		request.session['activities'] = []
		
	return render(request, "ninja_gold_app/index.html")

def create(request):
	building = request.POST['building']

	if building == 'farm':
		earnings = random.randint(10,20)
	elif building == 'cave':
		earnings = random.randint(5,10)
	elif building == 'house':
		earnings = random.randint(2,5)
	elif building == 'casino':
		earnings = random.randint(-50,50)
	print earnings
	request.session['count']+= earnings

	if earnings > 0:
		color = 'green'
		message = "Earned {} from a {}".format(earnings, building)
	else:
		color = 'red'
		message = "Entered a casino and lost {} golds ... Ouch...".format(earnings)

	activity = {'color': color, 'message': message}

	request.session['activities'].append(activity)

	return redirect('/')
