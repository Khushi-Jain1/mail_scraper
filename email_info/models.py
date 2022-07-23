from django.db import models

# Create your models here.

class EmailCategory(models.Model):
    category = models.CharField(max_length=50)
    default = models.CharField(max_length=1)
    name = models.CharField(max_length=50)