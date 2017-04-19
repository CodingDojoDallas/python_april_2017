# -*- coding: utf-8 -*-
from django.db import models

class Book(models.Model):
	title = models.CharField(max_length=45)
	author = models.CharField(max_length=45)
	published_date = models.DateTimeField()
	category = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	inprint = models.BooleanField(True)






# Create your models here.
