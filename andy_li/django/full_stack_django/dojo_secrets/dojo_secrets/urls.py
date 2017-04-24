from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r"^users$", views.createUser),
    url(r"^secrets$", views.secrets),
    url(r"^login$", views.loginUser),
    url(r"^logout$", views.logout),
    url(r"^posts$", views.createPost),
    url(r"^secrets/popular$", views.popular),
    url(r"^posts/likes/(?P<post_id>\d+)$", views.likePosts),
    url(r"^posts/delete/(?P<post_id>\d+)$", views.deletePosts),
]
