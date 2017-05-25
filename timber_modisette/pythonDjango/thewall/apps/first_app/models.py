from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(max_length=255)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "id: {} First Name: {} Last Name: {} Email: {} Password: {}".format(self.id, self.first_name, self.last_name, self.email, self.password)


class Message(models.Model):
	content = models.TextField()
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User)

	def __str__(self):
		return "id: {} message: {} user ID: {}".format(self.id, self.message, self.user_id)


class Comment(models.Model):
	content = models.TextField()
	created_at = models.DateTimeField(auto_now=True)
	updated_at = models.DateTimeField(auto_now=True)
	message_id = models.ForeignKey(Message, related_name='message')
	user = models.ForeignKey(User)

	def __str__(self):
		return "comment: {}".format(self.comment)



