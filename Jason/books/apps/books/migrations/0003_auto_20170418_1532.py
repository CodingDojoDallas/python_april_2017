# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_inprint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='inprint',
            field=models.BooleanField(verbose_name=True),
        ),
    ]