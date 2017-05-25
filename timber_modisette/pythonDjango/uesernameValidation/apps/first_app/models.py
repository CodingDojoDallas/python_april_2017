from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
	def validateUser(self,post):
		is_valid = True
		errors = []
		if len(post.get('username')) < 8 or len(post.get('username')) > 16:
			is_valid = False;
			errors.append('name field cannot be blank')
			
		else:
			is_valid = True
			
		return (is_valid, errors)


class User(models.Model):
	username = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	objects = UserManager()
