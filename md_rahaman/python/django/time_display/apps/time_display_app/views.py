from django.shortcuts import render
# import datetime
import pytz
# utc = pytz.utc
# from datetime import datetime 
import datetime
from pytz import timezone
fmt = "%B %d, %Y %I:%M %p"

# Create your views here.

def index(request):
	d = datetime.datetime.now(timezone('US/Central'))
	dtime=d.strftime(fmt)

	#datetime differnt format
	# print d.strftime("%A %d. %B %Y")
	# print dtime
	# print d.time().strftime("%I:%M %p")
	# print d.date().strftime("%B %d, %Y ")


	context = {
		"current_datetime":dtime
	}
  	return render(request, 'time_display_app/index.html',context)

