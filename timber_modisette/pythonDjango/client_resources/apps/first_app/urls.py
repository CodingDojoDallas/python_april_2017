from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^Showaddclient$', views.Showaddclient),
	url(r'^addclient$', views.addclient),
	url(r'^client/(?P<clientid>\d*)$', views.client),
	url(r'^showaddproject/(?P<clientid>\d*)$', views.showaddproject),
	url(r'^addproject(?P<clientid>\d*)$', views.addproject),
	url(r'^project/(?P<projectid>\d*)$', views.project),
	url(r'^addnote(?P<projectid>\d*)$', views.addnote),
	url(r'^deleteNote/(?P<noteid>\d*)$', views.deleteNote),

]