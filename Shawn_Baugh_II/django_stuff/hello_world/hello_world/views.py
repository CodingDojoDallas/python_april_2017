from django.shortcuts import render, HttpResponse
# Create your views here.
# index view
def index(request):
    print 'hello_world'
    return render(request, 'hello_world/index.html')
# end index view
