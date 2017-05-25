from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    context = {
    'books' : Book.objects.all()
    }
    return render(request, 'full_stack_books/index.html', context)

def create_book(request):
    is_valid = Book.objects.validate(request.POST)
    if type(is_valid) == dict:
        print 'we got errors'
    else:
        print 'we created a book'

    print '*'*50
    print 'result type is {}'.format(type(is_valid))
    print 'result value is {}'.format(is_valid)
    print '*'*50
    # books = Book.objects()

    return redirect('/')
