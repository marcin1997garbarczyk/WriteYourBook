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

    class Meta:
        model = Story
        fields = ['storyType', 'gender', 'characterName', 'inspiration', 'additionalPlotOutline', 'questionToChat']