from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Photodetails model that will be stored in the database
class PhotoDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    docfile = models.FileField()
    upload_date = models.DateTimeField('date uploaded',auto_now_add =True)
    caption = models.CharField(max_length=200)