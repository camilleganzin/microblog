# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your models here.
import datetime
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings

@python_2_unicode_compatible
class Userpost(models.Model):
	author = models.ForeignKey(settings.SOCIAL_AUTH_USER_MODEL,default=int(10))
	userpost_text = models.CharField(max_length=140)
	pub_date = models.DateTimeField(default=timezone.now)
	def __str__(self):
		return self.userpost_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
