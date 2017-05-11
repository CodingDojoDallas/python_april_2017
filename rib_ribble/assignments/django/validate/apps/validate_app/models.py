from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
	def validate(self, postData):
		if len(postData) > 8 and len(postData) < 16:
			return True
		else: 
			return False

class User(models.Model):
	user_name= models.CharField(max_length=255)
	email= models.CharField(max_length=255)
	created_at= models.DateTimeField(auto_now_add=True)
	updated_at= models.DateTimeField(auto_now=True)
	objects= UserManager()


		
