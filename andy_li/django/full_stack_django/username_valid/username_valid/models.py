# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class UserManager(models.Manager):
    def validate(self, post_data):
        valid = True
        error_msgs = []
        print post_data

        if not 8 <= len(post_data["username"]) <= 16:
            valid = False
            error_msgs.append("Username is invalid and must be between 8 - 16 characters.")

        if User.objects.filter(name = post_data["username"]):
            valid = False
            error_msgs.append("Username already used. Please enter a unique username.")

        return (valid, error_msgs)


class User(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "Name: {}, Created at: {}".format(self.name, self.created_at)

    objects = UserManager()
