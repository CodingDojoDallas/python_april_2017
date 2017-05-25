from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^secrets$', views.secrets),
	url(r'^postsecrets$', views.postsecrets),
	url(r'^favourites$', views.favourites),
	url(r'^deletesecrets/(?P<postid>\d*)$', views.deletesecrets),
	url(r'^like/(?P<postid>\d*)$', views.like),
	url(r'^likeonFavs/(?P<postid>\d*)$', views.likeonFavs),

]