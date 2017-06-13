from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r"^users/create$", views.createUser),
    url(r"^books$", views.books),
    url(r"^login$", views.loginUser),
    url(r"^logout$", views.logout),
    url(r"^books/add$", views.addBookReview),
    url(r"^books/create$", views.createBookReview),
    url(r"^books/(?P<book_id>\d+)$", views.showBook),
    url(r"^reviews/delete/(?P<rev_id>\d+)$", views.deleteBookReview),
    url(r"^reviews/create/(?P<book_id>\d+)$", views.createReview),
    url(r"^users/(?P<user_id>\d+)$", views.showUser),

]
