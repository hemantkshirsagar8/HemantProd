from django.db import models
from django.conf import settings
from fluent_contents.models import *
from fluent_contents.models.fields import PlaceholderField, PlaceholderRelation, ContentItemRelation
from ckeditor.fields import RichTextField

class Blog(models.Model):
	BlogID = models.AutoField(primary_key=True)
	Heading = models.CharField(max_length=200)
	Comments = models.CharField(max_length=20000)
	Status = models.CharField(max_length=20,choices=[('Active', 'Active'), ('In-Active', 'In-active')])
	CreateDate = models.DateField()
	class Meta:
	    db_table = u'Blog'
	    verbose_name_plural = "Blog"

	def __str__(self):
	    return self.Heading