from __future__ import unicode_literals
from django.db import models

class BookManager(models.Manager):
    def validate(self, post):
        print post
        result = {'errors':[], 'message':""}

        if len(post['title']) < 1:
            result['errors'].append('Title cannot be empty')
        elif len(post['category']) < 1:
            result['errors'].append('Category Cannot be crappy')
        elif len(post['author']) < 1:
            result['errors'].append('Author cant be bad')
        else:
            return Book.objects.create(title=post.get('title'), category=post.get('category'), author=post.get('author'))
        # return result

class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects=BookManager()
