from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^(?P<n>\d+)$', views.index),
]