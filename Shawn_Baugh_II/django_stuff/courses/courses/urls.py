from django.conf.urls import url, include
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course$', views.add_course),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^remove_page/(?P<id>\d+)$', views.remove_page),
]
