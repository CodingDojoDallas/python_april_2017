from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def validate(self, post):
        result = {'errors':[]}
        if len(post['first_name']) < 2 or len(post['last_name']) < 2:
            result['errors'].append('Please enter Name more than 2 characters')
            return result
        elif not re.search(r'\w+\@\w+\.\w+', post.get('email')):
            result['errors'].append('Please enter a valid email')
            return result
        elif len(post['password']) < 8:
            result['errors'].append('Password must be 8 or more characters')
            return result
        elif post['confirm_password'] != post['password']:
            result['errors'].append("Passwords don't match!!")
            return result
        else:
            return
    def create_user(self, post):
        user = User.objects.create(first_name=post.get('first_name'),last_name=post.get('last_name'), email=post.get('email'), password=post.get('password'))
        return user

    def login_validate(self, post):
        user = User.objects.filter(email=post.get('email')).first()
        if user and post['password'] == user.password:
            return {'status': True, 'user': user}
        else:
            return {'status': False, 'message': 'Please enter valid credintials'}

    def login(self, request, user):
        if ('user_id' not in request.session):
            request.session['user_id'] = user.id


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    post = models.TextField()
    like = models.ManyToManyField(User, related_name='liked_posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
