from django.shortcuts import render,redirect

# Create your views here.

def index(request):
	if 'attempts' not in request.session:
		request.session['attempts'] = 0
	return render(request,'survey_form_app/index.html')

def result(request):

	if request.method == 'POST':
		print '*'*50
		print request.POST
		context = {
			'name' : request.POST['name'],
			'location' : request.POST['location'],
			'favorite_language' : request.POST['favorite_language'],
			'comment' : request.POST['comment'],
		}
		request.session['attempts'] += 1 
		print request.session['attempts']
		print '*'*50
		return render(request,'survey_form_app/result.html',context)
	return redirect('/')
