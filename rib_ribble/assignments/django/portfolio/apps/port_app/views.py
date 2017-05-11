from django.shortcuts import render, redirect

def index(request):
	return render(request, "port_app/index.html")

def test(request):
	# return redirect('/')
	return render(request, "port_app/testimonial.html")
	


	
