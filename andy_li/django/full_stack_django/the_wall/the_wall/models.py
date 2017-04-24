# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "First name: {}, Last name: {}, e-mail: {}, Password: {}".format(self.first_name, self.last_name, self.email, self.password)

class Message(models.Model):
    user_id = models.ForeignKey(User)
    message = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "Message: {}".format(self.message)

class Comment(models.Model):
    message_id = models.ForeignKey(Message)
    user_id = models.ForeignKey(User)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "Comment: {}".format(self.comment)
