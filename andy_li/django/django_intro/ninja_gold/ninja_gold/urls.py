from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r"^process_money/(?P<clicked_bldg>\w+)$", views.process),
    url(r"^reset$", views.reset),
]
