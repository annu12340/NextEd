from django.db import models



class FlashCard(models.Model):
    owner = models.TextField()
    title = models.TextField()
    subject = models.TextField()
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

