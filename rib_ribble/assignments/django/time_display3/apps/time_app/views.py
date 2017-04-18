from django.shortcuts import render
from datetime import datetime

def index(request):
	context = {
		"time":datetime.now()
	}
	print context
	print "********"
	print context['time']
	return render(request, 'time_app/index.html', context) 
