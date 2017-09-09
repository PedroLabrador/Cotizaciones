# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class quotes(models.Model):
	id_number = models.AutoField(primary_key=True)
	name = models.CharField(max_length = 140)
	phone = models.CharField(max_length = 140)
	email = models.CharField(max_length = 140)
	type_info = models.CharField(max_length = 70)
	details =models.TextField()
	def __unicode__(self):
		return "%s - %s" % (self.id_number, self.name)