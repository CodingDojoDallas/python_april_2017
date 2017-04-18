
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('ninja_app.urls'))
]
