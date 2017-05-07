from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	print ("fucker")
	return render(request,'first_app/index.html')


def testimonials(request):
	print ('made it to testimonials')
	return render(request,'first_app/testimonials.html')


