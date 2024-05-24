from django.db import models

# Create your models here.

class Story(models.Model):
    storyType = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    characterName = models.CharField(max_length=200, blank=True)
    inspiration = models.CharField(max_length=200, blank=True)
    additionalPlotOutline = models.CharField(max_length=5000, blank=True)
    questionToChat = models.CharField(max_length=5000, blank=True)

