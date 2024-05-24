from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .Services.chatGptService import ChatGptService
from .Services.writerService import WriterService
from .models import Story
from .serializers import StoryFormSerializer

writerService = WriterService()
chatGptService = ChatGptService()

class SubmitStoryFormView(APIView):
    def post(self, request, format=None):
        print('HEHEHE')
        serializer = StoryFormSerializer(data=request.data)
        print('HEHEHEE')

        if(serializer.is_valid()):
            try:
                print('Jestem tu')
                newStoryObj = writerService.startYourOwnStory(Story, serializer)
                print('Mam nowy obiekt ')
                answerFromChat = chatGptService.askQuestionToChatGpt(newStoryObj.questionToChat)
                print('Odpowiedz z chatu : '+answerFromChat)
                return Response({'message': answerFromChat}, status=status.HTTP_201_CREATED, content_type='application/json')
            except(TypeError, ValueError, OverflowError, Story.DoesNotExist):
                print('EXECPTION 1')
                return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print('EXECPTION')
            return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


