from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Gwanjong(models.Model):
	word = models.CharField(unique=True, primary_key=True, max_length=256)
	value = models.IntegerField(default=0)