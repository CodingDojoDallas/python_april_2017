from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
	def validateUser(self, post_data):
		# print "im validating"
		# print post_data
		is_valid = True
		errors = []
		if len(post_data.get('first_name')) and len(post_data.get('last_name')) < 2:
			is_valid = False
			errors.append('name fields must be more than 2 characters')
		if not post_data.get('first_name').isalpha():
			is_valid = False
			errors.append('name fields must be only alphabetical letters')
		if not post_data.get('last_name').isalpha():
			is_valid = False
			errors.append('name fields must be only alphabetical letters')
		#if email is valid
		if not re.search(r'\w+\@\w+.\w+', post_data.get('email')):
			is_valid = False
			errors.append('must enter a valid email')
		#if password is greater than 8 characters, matches password confirmation
		if len(post_data.get('password')) < 9:
			is_valid = False
			errors.append('password must be more than 8 characters')
		if post_data.get('password_confirmation') != post_data.get('password'):
			is_valid = False
			errors.append('password and password confirmation must match')

		print (is_valid, errors)
		
		return (is_valid, errors)

	# def loginUser(self, post_data):
		# user = User.objects.filter(email = request.POST.get('email')).first()

		# if user and bcrypt.checkpw(request.POST.get('password').encode(), user.password):
		# 	request.session['user_id'] = user.id
		# 	return redirect('/success')
		# else: 
		# 	messages.error(request, 'invalid credentials')
		# 	return redirect('/')


class User(models.Model):
	first_name = models.CharField(max_length = 45)
	last_name = models.CharField(max_length = 45)
	email = models.CharField(max_length = 255)
	password = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	objects = UserManager()

	def __str__(self):
		return "first name:{}, last name:{}, email:{}, password:{}, created_at:{}, updated_at:{}".format(self.first_name, self.last_name, self.email, self.password, self.created_at, self.updated_at)
