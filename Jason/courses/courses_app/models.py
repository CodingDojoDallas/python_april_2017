# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Description(models.Model):
	description = models.CharField(max_length=255)

class Course(models.Model):
	name =  models.CharField(max_length=255)
	course_description = models.ForeignKey(Description)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "Name: {} Description: {} Date Added: {}}".format(self.name, self.description, self.date_added)



# Create your models here.
