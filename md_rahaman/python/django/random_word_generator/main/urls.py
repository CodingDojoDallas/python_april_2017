
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.random_word_generator_app.urls')),
]
