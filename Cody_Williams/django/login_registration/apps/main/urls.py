from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.createUser),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^posts$', views.createPost),
    url(r'^posts/likes/(?P<id>\d+)$', views.likePosts),
    url(r'^posts/(?P<id>\d+)$', views.showPosts),
    url(r'^comments/(?P<id>\d+)$', views.createComment),
    url(r'^posts/(?P<id>\d+)/delete$', views.deletePost),
    url(r'^secrets$', views.secrets),
]