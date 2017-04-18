from django.shortcuts import render

def index(request):
	return render(request, 'index.html')

def show_all(request):
	ninjas = {
	'image': 'images/tmnt.png'
	}
	return render(request, 'ninjas.html', ninjas)

def ninjas(request, color):
	context = {
	'orange': 'images/michelangelo.jpg',
	'red':'images/raphael.jpg',
	'purple': 'images/donatello.jpg',
	'blue' : 'images/blue.jpg',
	}
	if color in context:
		values = {
		'image': context[color]
		}
	else:
		values ={
		'image': 'images/notapril.jpg'
		}
	
	return render(request, 'ninjas.html', values)

