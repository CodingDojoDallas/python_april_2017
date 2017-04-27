from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^createUser$',views.createUser),
	url(r'^login$',views.login),
	url(r'^success$',views.success),
	url(r'^logout$',views.logout)
]