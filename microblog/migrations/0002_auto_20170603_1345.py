# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 11:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraction',
            name='userpost',
        ),
        migrations.AlterField(
            model_name='userpost',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.DeleteModel(
            name='Useraction',
        ),
    ]
