from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Course(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Description(models.Model):
	content = models.TextField(max_length=1000)
	course = models.ForeignKey(Course)
