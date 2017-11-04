# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

import uuid

# Create your models here.

class Rule(models.Model):
	rule_id = models.CharField(primary_key=True, max_length=64)
	rule_name = models.CharField(max_length=64)
	org = models.CharField(max_length=64)
	domain = models.CharField(max_length=64)
	sub_domain = models.CharField(max_length=64)
	rule_description = models.TextField()
	action = models.TextField()
	condition = models.TextField()
	created_on = models.DateTimeField(editable=False)
	modified_on = models.DateTimeField(editable=False)
	version = models.IntegerField(editable=False)

	def save(self, *args, **kwargs):
		if not self.rule_id:
			self.rule_id = uuid.uuid1().hex
			self.created_on = timezone.now()
			self.version = 1
		if not self.org:
			self.org = 'mastercard'
		if not self.domain:
			self.domain = 'payments'
		if not self.sub_domain:
			self.sub_domain = 'credits'

		self.modified_on = timezone.now()
		self.version += 1
		super(Rule, self).save(*args, **kwargs)


class RuleSet(models.Model):
	rule_set_id = models.CharField(primary_key=True, max_length=64)
	rule_id = models.ForeignKey('Rule', on_delete=models.CASCADE)
	rule_set_name = models.CharField(max_length=64)
	rule_set_description = models.TextField()
	created_on = models.DateTimeField(editable=False)
	modified_on = models.DateTimeField(editable=False)
	org = models.CharField(max_length=64)
	domain = models.CharField(max_length=64)
	sub_domain = models.CharField(max_length=64)

	def save(self, *args, **kwargs):
		if not self.rule_set_id:
			self.rule_set_id = uuid.uuid1().hex
			self.created_on = timezone.now()
		self.modified_on = timezone.now()

		if not self.org:
			self.org = 'mastercard'
		if not self.domain:
			self.domain = 'payments'
		if not self.sub_domain:
			self.sub_domain = 'credits'

		super(RuleSet, self).save(*args, **kwargs)



