from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return "id: {} first_name: {} last_name: {} email: {} password: {} created_at: {} updated_at: {}".format(self.id,self.first_name,self.last_name,self.email,self.password,self.created_at,self.updated_at)

class Message(models.Model):
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User)



class Comment(models.Model):
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	message_id = models.ForeignKey(Message,related_name = 'message')
	user = models.ForeignKey(User)
