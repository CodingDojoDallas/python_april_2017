from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^books$', views.success),
    url(r'^books/new$', views.new_book),
	url(r'^books/add$', views.add_book),
	url(r'^books/(?P<id>\d+)$', views.show_book),
	url(r'^users/(?P<id>\d+)$', views.user),
	url(r'^logout$', views.logout),
	url(r'^reviews/(?P<id>\d+)$', views.add_review),
	url(r'^delete/(?P<id>\d+)$', views.delete_review)
]