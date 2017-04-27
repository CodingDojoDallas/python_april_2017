from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	category = models.CharField(max_length=50)

	def __self__(self):
		return "title: {} author: {} category: {}".format(self.title, self.author, self.category)

