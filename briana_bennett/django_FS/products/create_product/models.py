from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length = 45)
	description = models.CharField(max_length = 255)
	weight = models.IntegerField() 
	price = models.DecimalField(decimal_places=2, max_digits=5)
	cost = models.DecimalField(decimal_places=2, max_digits=5)
	category = models.TextField()

	def __str__(self):
		return "name:{}, description:{}, weight:{}, price:{}, cost:{}, category:{}".format(self.name, self.description, self.weight, self.price, self.cost, self.category)
