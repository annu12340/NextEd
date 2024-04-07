from django.db import models



class Notes(models.Model):
    title=models.CharField(max_length=100)
    content = models.TextField()
    keywords = models.CharField(max_length=100)
    mnemonics  = models.TextField()
    questions  = models.TextField()
    simple_explanation  = models.TextField()
    owner = models.IntegerField()


