# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 07:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('microblog', '0002_auto_20170603_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpost',
            name='author',
            field=models.ForeignKey(default='author', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
