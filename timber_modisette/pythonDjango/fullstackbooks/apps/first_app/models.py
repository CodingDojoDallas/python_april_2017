from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Book(models.Model):
	title = models.CharField(max_length=200)
	category = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	