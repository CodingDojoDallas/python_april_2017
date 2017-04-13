from django.shortcuts import render, redirect
import random

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request,'main_app/index.html')

def process(request):
    if request.method == 'POST':
    	request.session['name'] = request.POST['name']
    	request.session['location'] = request.POST['location']
    	request.session['language'] = request.POST['language']
    	request.session['comment'] = request.POST['comment']
    	request.session['count'] += 1
    	return redirect('/result')
    return redirect('/')

def display(request):
    return render(request, 'main_app/result.html')
