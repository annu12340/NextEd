from django.db import models



class FlashCard(models.Model):
    noteid = models.IntegerField()
    question = models.TextField()
    answer = models.TextField()


