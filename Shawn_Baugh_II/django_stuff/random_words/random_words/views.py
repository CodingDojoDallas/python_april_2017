from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    print 'GETTING INFO'
    return render(request, 'random_words/index.html')

def generate(request):
    random_char = get_random_string(length=14)
    print random_char
    if 'number' not in request.session :
        request.session['number'] = 1
    else:
        request.session['number'] += 1
    print request.session['number']
    request.session['word'] = random_char
    return redirect('/')

def clear(request):
    request.session.clear()
    return render(request, 'random_words/index.html')
