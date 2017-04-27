from __future__ import unicode_literals

from django.db import models
import re

class UserManager(models.Manager):
	def validateUser(self, post):
		is_valid = True
		errors = []
		
		if User.objects.filter(email= post.get('email')).first() != None:
			is_valid = False
			errors.append('Need a brand new email')

		if len(post.get('first-name'))<2 and not re.search(r'\w+',post.get('first-name')):
			is_valid = False
			errors.append('Required; No fewer than 2 characters; letters only')

		if len(post.get('last-name'))<2 and not re.search(r'\w+',post.get('last-name')):
			is_valid = False
			errors.append('Required; No fewer than 2 characters; letters only')

		if not re.search(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$',post.get('email')):
			is_valid = False
			errors.append('Required; Valid Format')

		if len(post.get('password')) < 8 :
			is_valid = False
			errors.append('length should be more than 8 characters')

		if post.get('password') != post.get('passwordconfirm'):
			is_valid = False
			errors.append('password did not match')

		if post.get('email'):
			pass 
		return (is_valid, errors)


class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
