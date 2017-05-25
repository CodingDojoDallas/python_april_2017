from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def index(request):
	context = {
		'courses': Course.objects.all()
	}
	return render(request, 'courses_app/index.html', context)

def create(request):
	Course.objects.create(name = request.POST['name'], description = request.POST['description'])
	return redirect('/')

def delete_page(request, id):
	context = {
		'course': Course.objects.get(id = id)
	}

	return render(request, 'courses_app/delete.html', context)

def destroy_or_not(request, id):
	
	course = Course.objects.get(id = id)
	course.delete()

	return redirect('/')

