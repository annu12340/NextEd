from django.db import models

# Create your models here.

class Pet(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    owner = models.IntegerField()