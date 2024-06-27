from django.contrib import admin

from backendApp.models import Story, StoryMessage, UserWallet


# Register your models here.

@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ['pk','language','ownerId','storyTitle', 'storyType', 'gender', 'characterName', 'inspiration', 'additionalPlotOutline', 'questionToChat']

@admin.register(StoryMessage)
class StoryMessageAdmin(admin.ModelAdmin):
    list_display = ['pk', 'storyId', 'role', 'history', 'decisions', 'content', 'style']

@admin.register(UserWallet)
class UserWalletAdmin(admin.ModelAdmin):
    list_display = ['pk', 'ownerId', 'balance']