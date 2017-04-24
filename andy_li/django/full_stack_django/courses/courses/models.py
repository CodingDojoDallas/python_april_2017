# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length = 255)
    desc = models.TextField(max_length = 500)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return "Name: {}, Desc: {}, Created at: {}".format(self.name, self.desc, self.created_at)
