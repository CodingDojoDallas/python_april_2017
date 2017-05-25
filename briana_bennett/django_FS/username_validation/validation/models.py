from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def validateUser(self, post_data):
		print post_data
		is_valid = True
		errors = []
		if len(post_data.get('username')) < 8:
			is_valid = False
			errors.append('username cannot be less than 8 characters')
		return (is_valid, errors)

class User(models.Model):
	username = models.CharField(max_length = 15)
	created_at = models.DateTimeField(auto_now_add = True)
	objects = UserManager()

	def __str__(self):
		return "username:{}, created_at:{}".format(self.username, self.created_at)

