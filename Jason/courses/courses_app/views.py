# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,redirect
from models import Course

# Create your views here.


def index(request):
	if request.method == 'POST':
		description=Description.objects.create(description=request.POST['description'])
		course=Course.objects.create(name=request.POST['name'],course_description=description.id)
		# course.save()


	courses = Course.objects.all()
	courses.course_description.id
	return render(request,"courses/index.html",{"courses":courses})


def delete(request,id):
	Course.objects.get(id=id).delete()
	return redirect('/courses/destory/{}'.format(id),"courses/delete.html")

