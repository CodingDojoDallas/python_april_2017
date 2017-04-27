from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Books(models.Model):
	title = models.CharField(max_length=30)
	author = models.CharField(max_length=30)
	published_date = models.DateTimeField()
	category = models.CharField(max_length=30)
	in_print = models.BooleanField(True)

	def __str__(self):
		return "title: {} author: {} published_date: {} category: {} in_print: {}".format(self.title, self.author, self.published_date, self.category,self.in_print)
