from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Document(models.Model):
    docfile = models.FileField(upload_to='document/')

class UccDataUpload(models.Model):
    uccfile = models.FileField(upload_to='document/ucc/%m/%y/%d/')

class BoDataUpload(models.Model):
    bofile = models.FileField(upload_to='document/bo/%m/%y/%d/')

class MutualDataUpload(models.Model):
    mutualfile = models.FileField(upload_to='document/mutualequity/')