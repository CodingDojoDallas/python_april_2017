from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Products(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	weight = models.FloatField(max_length=100)
	price = models.FloatField(max_length=100)
	cost = models.FloatField(max_length=100)
	catagory = models.CharField(max_length=100)

	def __str__(self):
		return "Name: {} Description: {} weight: {} price: {} cost: {} catagory: {}".format(self.name, self.description, self.weight, self.price, self.cost, self.catagory)
