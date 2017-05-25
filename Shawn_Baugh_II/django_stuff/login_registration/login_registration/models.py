from __future__ import unicode_literals

from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
    def validate(self, post):
        print post.get('email')
        result = {'errors':[]}
        if len(post['first_name']) < 2 or len(post['last_name']) < 2:
            result['errors'].append('Name must be more then 2 characters')
            return result
        elif not re.search(r'\w+\@\w+\.\w+', post.get('email')):
            result['errors'].append('Give me a real email dude')
            return result
        elif len(post['password']) < 8:
            result['errors'].append('Need a longer password man')
            return result
        elif post['confirm_password'] != post['password']:
            result['errors'].append('Passwords gotta match')
            return result
        else:
            return User.objects.create(first_name=post.get('first_name'),last_name=post.get('last_name'), email=post.get('email'), password=post.get('password'))

    def login_user(self, post):
        # result = {'errors':[], 'messages':[]}
        user = User.objects.filter(email=post.get('email')).first()
        if user and post['password'] == user.password:
            return {'status': True, 'user': user}
        else:
            return {'status': False, 'message': 'Please enter valid email and/or password'}

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
