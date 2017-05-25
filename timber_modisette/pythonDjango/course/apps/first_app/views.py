from django.shortcuts import render, redirect
from .models import Course, Description
# Create your views here.

def index(request):
	print ('INDEX')
	context = {
	'description': Description.objects.all(), 
	}
	return render(request, 'first_app/index.html', context)


def process(request):
	print ('PROCESS')

	course = Course.objects.create(name=request.POST['name'])

	description = Description.objects.create(content=request.POST['description'], course=course)
	
	# description = Description.objects.all()

	# print description

	# print description.content
	# print description.course.name

	return redirect('/')



def remove(request, id):
	print ('REMOVE')

	
	description = Description.objects.get(id=id)
	context = {
	'description': description,
	# 'description' : description
	}

	
	

	return render(request, 'first_app/remove.html', context)


def delete(request,id):
	print ('DELETEEEE')
	


	description = Description.objects.get(id=id)
	course = description.course

	course.delete()
	description.delete()


	return redirect('/')



 



