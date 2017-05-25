from django.shortcuts import render, HttpResponse, redirect
import datetime
from django.utils.timezone import utc

# Create your views here.

def index(request):
	print('made it')
	now = datetime.datetime.now().strftime('%H:%M:%S')
	print now
	today = datetime.datetime.now().strftime('%m/%d/%y')
	print today

	dateTime = {
	'day': today,
	'time': now

	}
	

	return render(request, 'first_app/index.html', dateTime)