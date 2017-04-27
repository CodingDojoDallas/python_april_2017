from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Description(models.Model):
	description = models.CharField(max_length=200)

	def __str__(self):
		return "description: {}".format(self.description)

class Course(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateField(auto_now_add=True)
	description = models.ForeignKey(Description)

	def __str__(self):
		return "name: {} created_at: {} id:{} description: {}".format(self.name,self.created_at,self.id,self.description)



