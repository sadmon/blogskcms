#-*- coding: utf-8 -*-
from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=150, verbose_name="Title")
	content = models.TextField(verbose_name="Text")
	published = models.DateTimeField(verbose_name="Publication date")
	image = models.FileField(upload_to="images/", verbose_name="image")

	def __unicode__(self):
		return self.title

class Comment(models.Model):
	name = models.CharField(max_length=150, verbose_name="User")
	content = models.TextField(verbose_name="Comment")
	published = models.DateTimeField(verbose_name="Publication date")
	article = models.ForeignKey(Article)

	def __unicode__(self):
		return self.name


