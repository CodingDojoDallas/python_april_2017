# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-18 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20170418_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='in_print',
            field=models.NullBooleanField(),
        ),
    ]
