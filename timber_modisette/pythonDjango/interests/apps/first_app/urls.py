from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^processUserAndInterest$', views.processUserAndInterest),
	url(r'^show$', views.show),
	url(r'^userProfile/(?P<userid>\d*)$', views.userProfile),
	url(r'^delete/(?P<interest>\w*)$', views.delete),


]