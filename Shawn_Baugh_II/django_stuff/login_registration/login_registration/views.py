from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'login_registration/index.html')

def process(request):
    # pass
    is_valid = User.objects.validate(request.POST)
    if type(is_valid) == dict:
        print '*'*50
        print is_valid
        print '*'*50
        for error in is_valid['errors']:
            messages.error(request, error)
        return redirect('/')
    return redirect('/success')

def login(request):
    is_valid = User.objects.login_user(request.POST)
    if is_valid['status'] == True:
        request.session['id'] = is_valid['user'].id
    else:
        if is_valid['status'] == False:
            is_valid['message']
            return redirect('/')
    return redirect('/success')

def success(request):
    print 'id', request.session['id']
    user = User.objects.get(id=request.session['id'])
    print user
    return render(request, 'login_registration/success.html', {'user':user})
