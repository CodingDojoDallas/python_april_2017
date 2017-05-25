from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def validate(self, post):
        result = {'errors':[]}

        if len(post['name']) <= 0:
            result['errors'].append('Name must have characters')
            return result
        else:
            return User.objects.create(name=post.get('name'))

class User(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
