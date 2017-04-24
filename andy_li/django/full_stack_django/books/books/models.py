# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    pub_date = models.DateField()
    category = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    in_print = models.BooleanField()

    def __str__(self):
        return "Title: {}, Author: {}, Published Date: {}, Category: {}".format(self.title, self.author, self.pub_date, self.category)
