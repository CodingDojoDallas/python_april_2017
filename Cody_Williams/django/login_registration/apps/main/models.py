from __future__ import unicode_literals

from django.db import models
import re, bcrypt
# Create your models here.
class UserManager(models.Manager):
	def validateUser(self, post):
		is_valid = True
		errors = []
		if len(post.get('name')) == 0:
			is_valid = False
			errors.append('Name field cannot be blank')
		if not re.search(r'\w+\@\w+\.\w+', post.get('email')):
			is_valid = False
			errors.append('You must provide a valid email address')
		if len(post.get('password')) == 0:
			is_valid = False
			errors.append('Password cannot be blank')
		if post.get('password') != post.get('password_confirmation'):
			is_valid = False
			errors.append('Your passwords do not match')
		return (is_valid, errors)

	def loginUser(self, post):
		user = User.objects.filter(email=post.get('email')).first()
		if user and bcrypt.checkpw(post.get('password').encode(), user.password.encode()):
			return {'status': True, 'user': user}
		else:
			return {'status': False, 'message': 'invalid credentials'}

class PostManager(models.Manager):
	def validatePost(self, post):
		is_valid = True
		errors = []
		if len(post.get('post')) == 0:
			is_valid = False
			errors.append('Post must not be blank')
		return {'status': is_valid, 'errors': errors}

class User(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Post(models.Model):
	post = models.TextField()
	user = models.ForeignKey(User, related_name="posts")
	likes = models.ManyToManyField(User, related_name="posts_liked")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = PostManager()

class Comment(models.Model):
	comment = models.TextField()
	post = models.ForeignKey(Post, related_name="comments")
	user = models.ForeignKey(User, related_name="comments")
	likes = models.ManyToManyField(User, related_name="comments_liked")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
