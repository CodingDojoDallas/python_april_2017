from django.shortcuts import render

import datetime


# Create your views here.
def index(request):
	date_time = {
		'time':datetime.datetime.now().strftime('%I:%M %p'),
		'date':datetime.datetime.now().strftime('%b %d, %Y')
	}
	
	return render(request, 'timedisplay/index.html', date_time)
