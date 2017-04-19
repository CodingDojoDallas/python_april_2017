# -*- coding: utf-8 -*-
from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=38)
	description = models.TextField()
	weight = models.FloatField()
	price = models.FloatField()
	cost = models.FloatField()
	category = models.CharField(max_length=45)
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "Name: {} \nDescription: {} \nWeight: {}".format(self.name, self.description, self.weight)

	def laugh(self):
		return "hahahahahahahaahaha"


# Create your models here.
