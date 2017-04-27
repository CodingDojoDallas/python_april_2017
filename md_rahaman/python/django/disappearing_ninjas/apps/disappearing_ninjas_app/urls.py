
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'ninjas/(?P<color>\w\D+)$', views.ninjas),
	url(r'^ninjas$', views.ninjas),
	url(r'^$', views.index)
]

# ?P<color>\w+$