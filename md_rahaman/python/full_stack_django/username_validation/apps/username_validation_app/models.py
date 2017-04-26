from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserManager(models.Manager):
	def name_validation(self,name):
		if len(name)>8 and len(name)<16:
			print True
			return True
		else:
			return False


class User(models.Model):
	name = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "name: {} created_at: {}".format(self.name,self.created_at)
	objects = UserManager()
