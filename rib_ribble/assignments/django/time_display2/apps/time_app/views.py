from django.shortcuts import render
import datetime

def index(request):
	context = {
		'time': datetime.datetime.now()
	}
	return render(request,'time_app/index.html',context)
