from django.db import models

# Create your models here.
class Feature(models.Model):
    Name = models.CharField(max_length=100, default='')
    Details = models.CharField(max_length=500, default='')

class Subscribe(models.Model):
    Mail = models.CharField(max_length=100, default='')

