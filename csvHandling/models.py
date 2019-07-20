from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    userId = models.CharField(max_length=50)
    userPassword = models.CharField(max_length=15)
