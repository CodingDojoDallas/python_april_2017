from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    context = {
    'courses' : Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add_course(request):
    Course.objects.create(name=request.POST.get('name'), description=request.POST.get('description'))
    return redirect('/')

def remove_page(request, id):
    course = Course.objects.get(id=id)

    return render(request, 'courses/remove.html',{'course':course})

def remove(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
