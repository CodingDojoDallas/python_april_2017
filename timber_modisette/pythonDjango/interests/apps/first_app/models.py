from __future__ import unicode_literals

from django.db import models

# Create your models here.


class UserManager(models.Manager):
	def validateUser(self,post):
		is_valid = True
		errors =[]
		
		if len(post.get('name')) == 0:
			is_valid = False
			errors.append("Must enter valid name")
		if len(post.get('interest')) == 0:
			is_valid = False
			errors.append("Must enter valid interest")
		return (is_valid, errors)








class User(models.Model):
	name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()


class Interest(models.Model):
	content = models.CharField(max_length=255)
	user = models.ManyToManyField(User, related_name='interests')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)