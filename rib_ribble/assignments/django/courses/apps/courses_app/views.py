from django.shortcuts import render, redirect
from models import Course

def index(request):
	courses = Course.objects.all()
	print ("**QUERY RESULT**:", courses)
	context = {
		"courses": courses
	}
	return render(request, "courses_app/index.html", context)

def input(request):
	Course.objects.create(name=request.POST ['name'], description=request.POST ['description'])
	return redirect('/')

def confirm(request, id):
	print ("**ROUTE PARAM**", id)
	course = Course.objects.get(id= id)
	print ("**QUERY RESULT**", course)
	context = {
		"course": course
	}
	return render(request, "courses_app/confirm.html", context)

def delete(request, id):
	print ("**ROUTE PARAM**", id)
	Course.objects.get(id=id).delete()
	return redirect ('/') 



