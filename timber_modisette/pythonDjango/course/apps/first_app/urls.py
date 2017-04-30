from django.conf.urls import url 
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^process$', views.process),
	url(r'^remove(?P<id>\d+)$', views.remove),
	url(r'^delete/(?P<id>\d+)$', views.delete)
]