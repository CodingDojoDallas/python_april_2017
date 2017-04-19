from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    print 'GETTING INDEX ROUTE'
    return render(request, 'survey_form/index.html')

def result(request):
    return render(request, 'survey_form/result.html')

def process(request):
    if 'number' not in request.session :
        request.session['number'] = 1
    else:
        request.session['number'] += 1

    data = {
    'name' : request.POST['name'],
    'location' : request.POST['location'],
    'favorite_language' : request.POST['favorite_language'],
    'comment' : request.POST['comment']
    }
    request.session['user'] = data

    print request.POST
    return redirect('/result')

def clear(request):
    request.session.clear()
    return redirect('/')
