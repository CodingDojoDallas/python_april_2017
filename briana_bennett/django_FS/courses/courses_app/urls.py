from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^courses/(?P<id>\d+)/delete$', views.delete_page),
    url(r'^courses/(?P<id>\d+)/destroy$', views.destroy_or_not),
]