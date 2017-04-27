
from django.conf.urls import url
from . import views

#CONTROLLER!!!

#Models --viess -- TEMPLATES

urlpatterns = [
	url(r'^$', views.index),
	url(r'^result$', views.result),
]