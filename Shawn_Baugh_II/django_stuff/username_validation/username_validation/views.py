from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'username_validation/index.html')

def process(request):
    is_valid = User.objects.validate(request.POST)
    if type(is_valid) == dict:
        print '*'*50
        print is_valid
        print '*'*50
        for error in is_valid['errors']:
            messages.error(request, error)
        return redirect('/')
    return redirect('/success')

def success(request):
    context = {
    'users' : User.objects.all()
    }
    return render(request, 'username_validation/success.html', context)
