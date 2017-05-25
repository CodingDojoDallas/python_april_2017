from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
	print ('made it to index')
	if 'count' not in request.session:
		request.session['count'] = 0

	return render(request, 'first_app/index.html')


def process(request):
	if request.method == 'POST':
		print ("made it to process")

		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['dropLocation']
		request.session['favlan'] = request.POST['dropFav']
		request.session['comment'] = request.POST['comment']
		request.session['count'] = request.session['count'] + 1

		return redirect('/show')

	else:
		return redirect('/')

def show(request):
	print ('made it to the show')

	return render(request, 'first_app/show.html')