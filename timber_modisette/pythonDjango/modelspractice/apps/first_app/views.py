from django.shortcuts import render, HttpResponse, redirect
from .models import People
# Create your views here.
def index(request):
	print ('INDEX')
	

	People.objects.create(first_name='Timber', last_name='modisette')
	people = People.objects.all()
	print people

	return render(request, 'first_app/index.html')