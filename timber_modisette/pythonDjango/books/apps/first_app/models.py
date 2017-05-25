from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	published_date = models.DateTimeField()
	category = models.CharField(max_length=100)
	in_print = models.BooleanField(True)

	def __str__(self):
		return "Title: {} Author: {} Published date: {} Category: {} In print: {}".format(self.title, self.author, self.published_date, self.category, self.in_print)


