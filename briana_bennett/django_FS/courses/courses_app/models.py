from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Course(models.Model):
	name = models.CharField(max_length = 45)
	description = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return	"name:{}, description:{}, created_at{},".format(self.name, self.description, self.created_at)