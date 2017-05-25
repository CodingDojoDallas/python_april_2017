from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^login$', views.login),
    url(r'^secrets$', views.secrets),
    url(r'^create_post$', views.create_post),
    url(r'^like_post/(?P<id>\d+)$', views.like_post),
    url(r'^delete_post/(?P<id>\d+)$', views.delete_post),
    url(r'^popular$', views.popular),
    url(r'^logout$', views.logout),

]
