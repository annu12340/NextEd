from django.db import models



class Notes(models.Model):
    title=models.CharField(max_length=100)
    content = models.TextField()
    keywords = models.CharField(max_length=100)
    mnemonics  = models.CharField(max_length=500)
    owner = models.IntegerField()


