from rest_framework import serializers

from .models import Story

class StoryFormSerializer(serializers.ModelSerializer):

    def getStoryType(self, obj):
        return obj.storyType

    def getGender(self, obj):
        return obj.gender

    def getCharacterName(self, obj):
        return obj.characterName

    def getInspiration(self, obj):
        return obj.inspiration

    def getAdditionalPlotOutline(self, obj):
        return obj.additionalPlotOutline

    def getQuestionToChat(self, obj):
        return obj.questionToChat

    def getTitle(self, obj):
        return obj.title

    def getLanguage(self, obj):
        return obj.language

    class Meta:
        model = Story
        fields = ['storyTitle', 'language', 'storyType', 'gender', 'characterName', 'inspiration', 'additionalPlotOutline', 'questionToChat']
