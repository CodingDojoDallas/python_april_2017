from __future__ import unicode_literals
from django.db import models
import re

class ClientManager(models.Manager):
	def validateClient(self, post):
		is_valid = True
		errors = []
		if len(post.get('business_name')) < 2:
			is_valid = False
			errors.append("please enter a valid Business Name")
		if not re.search(r'\w+\@+\w+\.\w+', post.get('email')):
			is_valid = False
			errors.append("Please enter a valid email address")
		number = str(post.get('phone'))
		if len(number) < 10:
			is_valid=  False
			errors.append('please enter a valid 10 digit number')
		return (is_valid,errors)



class Client(models.Model):
	name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	phone = models.IntegerField()
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ClientManager()


class ProjectManager(models.Manager):
	def validateProject(self, post):
		is_valid = True
		errors = []
		if len(post.get('project_name')) < 2:
			is_valid = False
			errors.append('please enter a valid project')
		return (is_valid, errors)



class Project(models.Model):
	title = models.CharField(max_length=255)
	client = models.ForeignKey(Client, related_name="projects")
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ProjectManager()

class NoteManager(models.Manager):
	def validateNote(self, post):
		is_valid = True
		errors = []
		if len(post.get('add_note')) < 10:
			is_valid = False
			errors.append('please enter a valid note')
			print "hello"
		return (is_valid, errors)

class Note(models.Model):
	content = models.TextField(max_length=500)
	project = models.ForeignKey(Project, related_name="notes")
	create_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = NoteManager()



