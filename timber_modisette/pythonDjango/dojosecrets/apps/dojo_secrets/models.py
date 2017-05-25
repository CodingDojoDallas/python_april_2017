from __future__ import unicode_literals

from django.db import models
import re
# Create your models here.

class UserManager(models.Manager):
	def validateUser(self,post):
		is_valid = True
		errors =[]
		if len(post.get('first_name')) == 0:
			is_valid = False
			errors.append("Must enter valid first name")

		if len(post.get('last_name')) == 0:
			is_valid = False
			errors.append("Must enter valid last name")

		if not re.search(r'\w+\@+\w+\.\w+', post.get('email')):
			is_valid = False
			errors.append("Please enter a valid email address")

		if User.objects.filter(email=post.get('email')).first() != None:
			is_valid = False
			errors.append("email already exists")

		if len(post.get('password')) < 6:
			is_valid = False
			errors.append("please enter a password of at least 6 characters")

		if post.get('password') != post.get('cf_password'):
			is_valid = False
			errors.append("passwords do not match")

		return (is_valid, errors)




class User(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.EmailField(max_length=200)
	password = models.CharField(max_length=100)
	cf_password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()




class Post(models.Model):
	content = models.TextField(max_length=1000)
	user = models.ForeignKey(User, related_name='posts')
	likes = models.ManyToManyField(User, related_name='liked_posts')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


