from django.shortcuts import render, HttpResponse
import datetime
# Create your views here.
def index(request):
    print 'GETTING INFO HERE!!'
    current = {
        'day' : datetime.datetime.now()
    }

    return render(request, 'time_display/index.html', current)
