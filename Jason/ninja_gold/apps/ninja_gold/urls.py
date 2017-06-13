from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index),
	#url(r'^process_money',views.process_money),
	url(r'^/process_money/(?P<location>\w+)$', views.process_money)
]