# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	author = models.CharField(max_length=255)
	created_at =models.DateTimeField(auto_now_add=True)
	updated_at =models.DateTimeField(auto_now=True)

	def __str__(self):
		return "Title: {} Author: {} Category: {}".format(self.author, self.category,self.author)




# Create your models here.
