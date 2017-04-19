from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):


	return render(request, 'ninjagold/index.html')

def process_money(request):

	if request.method == 'POST':
	
		#add gold amount to gold in session
		if 'gold' not in request.session:
			request.session['gold'] = 0
		if 'activities' not in request.session:
			request.session['activities'] = []
		
		if request.POST['name'] == 'farm':
			gold = random.randint(10,20)
			request.session['gold'] += gold
		
		elif request.POST['name'] == 'cave':
			gold = random.randint(5,10) 
			request.session['gold'] += gold
		
		elif request.POST['name'] == 'house':
			gold = random.randint(2,5)
			request.session['gold'] += gold

		
		elif request.POST['name'] == 'casino':
			gold = random.randint(-50,50)
			request.session['gold'] += gold
			
		messageObj = {}
		if gold < 0:
			messageObj['color'] = 'red'
			messageObj['message'] = "Lost {} gold from the {}".format(abs(gold), request.POST['name'])
		else:
			messageObj['color'] = 'green'
			messageObj['message'] = "Earned {} gold from the {}".format(abs(gold), request.POST['name'])	

		#Append message to request.session['activities']
		request.session['activities'].insert(0, messageObj)

	print request.session['gold']
	print request.session['activities']
	print request.session['activities']

	return redirect('/')


def reset(request):
	request.session.clear()

	return redirect('/')















