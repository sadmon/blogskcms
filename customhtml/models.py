#-*- coding: utf-8 -8-
from django.db import models

class CustomHtml(models.Model):
	title = models.CharField(max_length=150, verbose_name="Title")
	sourcehtml = models.TextField(verbose_name="HTML Code")

	def __unicode__(self):
		return self.title
