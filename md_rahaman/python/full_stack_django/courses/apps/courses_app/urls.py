from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^add$',views.add),
	url(r'^courses/confirm_destroy/(?P<id>\d+)$',views.confirm_destroy),
	url(r'destroy$',views.destroy)
]