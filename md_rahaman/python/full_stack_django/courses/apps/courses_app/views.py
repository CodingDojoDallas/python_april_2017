from django.shortcuts import render, redirect
from .models import Course,Description


# Create your views here.

def index(request):
	# courses = Course.objects.all()
	description = Description.objects.all()
	print Description
	# for  in courses:
	# 	print course


	context={
		"courses": Course.objects.all()
	} 
	return render(request, "courses_app/index.html",context)

def add(request):
	description = Description.objects.create(description=request.POST['description'])
	course = Course.objects.create(name=request.POST['name'],description=description)

	return redirect('/')

def confirm_destroy(request,id):
	if id not in request.session:
		request.session['id'] = id
	context = {
		"course": Course.objects.get(id=id)
	}

	return render(request,'courses_app/destroy.html',context)


def destroy(request):
	course = Course.objects.get(id=request.session['id'])
	print course
	print request.session['id']
	course.delete()

	request.session.pop('id',None)

	return redirect('/')





