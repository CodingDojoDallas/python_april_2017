from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r"^gen$", views.gen),
    url(r"^reset$", views.reset),
]
