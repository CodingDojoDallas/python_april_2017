from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, 'surveyform_app/index.html')

def surveys_process(request, methods=['POST']):
	form_data = {
		'name': request.POST['name'],
		'dojo_location': request.POST['dojo_location'],
		'favorite_language': request.POST['favorite_language'],
		'comment': request.POST['comment']
	}

	if request.method == 'POST':
		request.session['form_data'] = form_data

	if 'count' not in request.session:
		request.session['count'] = 0
	else: 
		request.session['count'] += 1

	return redirect('/result')
	

def result(request):

	return render(request, 'surveyform_app/result.html')
	