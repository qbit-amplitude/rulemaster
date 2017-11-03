# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import uuid

# Create your models here.

class Rule(models.Model):
	rule_id = models.CharField(primary_key=True, max_length=64)
	rule_name = models.CharField(max_length=64)
	rule_description = models.TextField()
	action = models.TextField()
	condition = models.TextField()
	created_on = models.DateTimeField(editable=False)
	modified_on = models.DateTimeField(editable=False)
	version = models.IntegerField()

	def save(self, *args, **kwargs):
		if not self.rule_id:
			self.rule_id = uuid.uuid1().hex
			self.created_on = timezone.now()
			self.version = 1
		self.modified_on = timezone.now()
		self.version += 1
		return super(Rule, self).save(*args, **kwargs)


class RuleSet(models.Model):
	rule_set_id = models.CharField(primary_key=True, max_length=64)
	rule_id = models.ForeignKey('Rule')
	rule_set_name = models.CharField(max_length=64)
	rule_set_description = models.TextField()
	created_on = models.DateTimeField(editable=False)
	modified_on = models.DateTimeField(editable=False)

	def save(self, *args, **kwargs):
		if not self.rule_set_id:
			self.rule_set_id = uuid.uuid1().hex
			self.created_on = timezone.now()
		self.modified_on = timezone.now()
		return super(Rule, self).save(*args, **kwargs)



