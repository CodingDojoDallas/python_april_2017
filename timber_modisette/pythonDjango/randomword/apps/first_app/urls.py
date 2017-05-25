from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^randomWord$', views.randomWord),
	url(r'^popAttempts$', views.popAttempts),
]