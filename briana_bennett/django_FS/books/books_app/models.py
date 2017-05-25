from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length = 45)
	author = models.CharField(max_length = 255)
	published_date = models.DateField(max_length = 45)
	category = models.CharField(max_length = 45)
	in_print = models.BooleanField()

	def __str__(self):
		return "title:{}, author:{}, published_date:{}, category:{}, in_print{}".format(self.title, self.author, self.published_date, self.category, self.in_print)