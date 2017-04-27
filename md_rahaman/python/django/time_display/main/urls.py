
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.time_display_app.urls')),
]
