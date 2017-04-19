from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^surveys/process$', views.surveys_process),
    url(r'^result$', views.result)
]