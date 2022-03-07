from django.db import models

# Create your models here.

class Webpage(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    added = models.DateTimeField(auto_now=True)
    link = models.CharField(max_length=250)
