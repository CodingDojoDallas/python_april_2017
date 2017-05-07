from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^ninja/(?P<color>\w*)$', views.show)
]