from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	print ('made it to index')
	
	return render(request, 'first_app/index.html')

def show(request, color):
	print ('made it to show')

	request.session['color'] = color

	print request.session['color']

	return render(request, 'first_app/show.html')