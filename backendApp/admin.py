from django.contrib import admin

from backendApp.models import Story


# Register your models here.

@admin.register(Story)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['pk', 'storyType', 'gender', 'characterName', 'inspiration', 'additionalPlotOutline', 'questionToChat']