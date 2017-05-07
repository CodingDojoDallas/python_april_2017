from django.shortcuts import render, HttpResponse, redirect
# do not forget that if you want to use redirect, you must first import it

# Create your views here.
def index(request):
	print ("made it to the index page")
	return render(request, 'first_app/index.html')

def projects(request):
	print ('made it to the projects page!')
	return render(request, 'first_app/projects.html')

def aboutme(request):
	print ('made it to the fuckin about me section! and I still cant spell!')
	return render(request, 'first_app/aboutme.html')

def testimonials(request):
	print('fucka youa!')
	return render(request, 'first_app/testimonials.html')

def create(request):
	if request.method == 'POST':
		print '*'*50
		print request.method
		print request.POST
		print '*'*50
		request.session['name'] = request.POST['first_name']
		return redirect('/')
	else:
		return redirect('/')
