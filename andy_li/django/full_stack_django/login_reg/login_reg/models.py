# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re, bcrypt

class UserManager(models.Manager):
    def validateUserReg(self, post_data):
        valid = True
        error_msgs = []
        print post_data

        if len(post_data["first_name"]) < 2 or not post_data["first_name"].isalpha():
            valid = False
            error_msgs.append("First name must be at least 2 characters and only letters.")
        if len(post_data["last_name"]) < 2 or not post_data["last_name"].isalpha():
            valid = False
            error_msgs.append("Last name must be at least 2 characters and only letters.")
        if not re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", post_data["email"]):
            valid = False
            error_msgs.append("Invalid e-mail.")
        if len(post_data["password"]) < 8:
            valid = False
            error_msgs.append("Passwords must be at least 8 characters long.")
        if post_data["password"] != post_data["confirm_pwd"]:
            valid = False
            error_msgs.append("Passwords don't match.")

        return {"pass": valid, "errors": error_msgs}

    def validateUserLog(self, post_data):
        # verify email, password against db for valid user
        user = User.objects.filter(email = post_data["email"]).first()

        if user and bcrypt.checkpw(post_data["password"].encode(), user.password.encode()):
            return {"pass": True, "user": user}

        return {"pass": False, "errors": "Invalid login credentials."}


class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __str__(self):
        return "First name: {}, Last name: {}, e-mail: {}, Password: {}".format(self.first_name, self.last_name, self.email, self.password)
