from django.shortcuts import render,redirect
import datetime

# Create your views here.

def ninjas(request, color='tmnt'):
	if color not in ['red', 'blue', 'orange', 'purple', 'tmnt']:
		color = 'notapril'

  	return render(request, 'disappearing_ninjas_app/ninjas.html', {'color': color})

def index(request):
	return render(request, 'disappearing_ninjas_app/index.html')


