# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class HeUser(User):
	user = models.OneToOneField(User)
	hit_count = models.IntegerField(null=False, blank=False)
	tmin = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

