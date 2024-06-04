from django.contrib import admin

from backendApp.models import Story, StoryMessage


# Register your models here.

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['pk','storyTitle', 'storyType', 'gender', 'characterName', 'inspiration', 'additionalPlotOutline', 'questionToChat']

@admin.register(StoryMessage)
class StoryMessageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'storyId', 'role', 'content']