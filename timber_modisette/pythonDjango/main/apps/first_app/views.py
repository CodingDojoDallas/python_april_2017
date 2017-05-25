from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	print ('*'*100)
	return render(request, 'first_app/index.html')