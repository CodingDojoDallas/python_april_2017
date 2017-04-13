from django.shortcuts import render, HttpResponse
import datetime
# Create your views here.
def index(request):
    context = {
    "time":datetime.datetime.now()
    }

    return render(request, 'main_app/index.html', context)
#%B %e %Y %I:%M%p
