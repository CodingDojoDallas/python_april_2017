from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r"^create$", views.create),
    url(r"^success$", views.success),
    url(r"^login$", views.login),
    url(r"^logout$", views.logout),
]
