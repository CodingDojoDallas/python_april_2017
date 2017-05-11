from django.shortcuts import render

def index(request):
	return render(request, "hello_world_app/index.html")
