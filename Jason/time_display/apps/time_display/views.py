# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse
import datetime

def index(request):
	context = {
		"current_date": datetime.datetime.now().date(),
		"current_time": datetime.datetime.now().time(),
	}

	return render(request,'time_display/index.html',context)

# Create your views here.
