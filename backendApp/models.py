from django.db import models

# Create your models here.

class Story(models.Model):
    storyTitle = models.CharField(max_length=200, blank=True)
    storyType = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    characterName = models.CharField(max_length=200, blank=True)
    inspiration = models.CharField(max_length=200, blank=True)
    additionalPlotOutline = models.CharField(max_length=5000, blank=True)
    questionToChat = models.CharField(max_length=5000, blank=True)

class StoryMessage(models.Model):
    storyId = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    content = models.CharField(max_length=500000)
