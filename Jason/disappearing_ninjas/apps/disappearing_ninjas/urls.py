from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^ninjas$',views.display_all),
	url(r'^ninjas/(?P<color>[a-z]+)$',views.display_color),
]
