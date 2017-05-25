from django.shortcuts import render, redirect
from .models import User, Message, Comment

# Create your views here.
def index(request):


	return render(request, 'the_wall_app/index.html')