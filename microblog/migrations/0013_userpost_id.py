# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0012_auto_20170604_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='id',
            field=models.IntegerField(default=0),
        ),
    ]