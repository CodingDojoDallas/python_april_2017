from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^create_post$', views.create_post),
    url(r'^popular_posts$', views.popular_posts),
    url(r'^delete_post/(?P<id>\d+)$', views.delete_post),
    url(r'^posts/likes/(?P<id>\d+)$', views.like_post),

]