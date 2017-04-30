from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^homepage$', views.homepage),
	url(r'^login$', views.login),
	url(r'^addbook$', views.addbook),
	url(r'^createbook$', views.createbook),
	url(r'^book/(?P<bookid>\d*)$', views.book),
	url(r'^addbookreview/(?P<bookid>\d*)$', views.addbookreview),
	url(r'^deletereview/(?P<reviewid>\d*)$', views.deletereview),
	url(r'^deletebookreview/(?P<reviewid>\d*)$', views.deletebookreview),
	url(r'^logout$', views.logout),
	url(r'^userprofile/(?P<userid>\d*)$', views.userprofile),


	# url(r'^book/(?P<bookid>\d*)$', views.addreview),
	# url(r'^logout$', views.logout),
	# url(r'^secrets$', views.secrets),
	# url(r'^postsecrets$', views.postsecrets),
	# url(r'^favourites$', views.favourites),
	# url(r'^deletesecrets/(?P<postid>\d*)$', views.deletesecrets),
	# url(r'^like/(?P<postid>\d*)$', views.like),
	# url(r'^likeonFavs/(?P<postid>\d*)$', views.likeonFavs),

]