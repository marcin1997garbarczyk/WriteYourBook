from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .Services.chatGptService import ChatGptService
from .Services.writerService import WriterService
from .models import Story, StoryMessage
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
                writerService.saveStoryMessageToDb(StoryMessage, newStoryObj.pk, 'user', newStoryObj.questionToChat)

                answerFromChat = chatGptService.askQuestionToChatGpt(newStoryObj.questionToChat)
                print('Odpowiedz z chatu : '+answerFromChat)
                writerService.saveStoryMessageToDb(StoryMessage, newStoryObj.pk, 'assistant', answerFromChat)
                return Response({'message': answerFromChat, 'storyId': newStoryObj.pk}, status=status.HTTP_201_CREATED, content_type='application/json')
            except(TypeError, ValueError, OverflowError, Story.DoesNotExist):
                print('EXECPTION 1')
                return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print('EXECPTION')
            return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class SubmitAnswerFromUserView(APIView):
    def post(self, request, format=None):
        print('HEHEHE')
        dataFromRequest = request.data
        print(f'data from request {dataFromRequest}')

        try:
            chatGptService.injectStoryOfTalkWithRobot(StoryMessage, dataFromRequest.get('storyId'))
            writerService.saveStoryMessageToDb(StoryMessage, dataFromRequest.get('storyId'), 'user', dataFromRequest.get('answer'))
            print('NIMA 1')
            for message in chatGptService.chatMessages:
                print(f' message from chat {message}')
            print('NIMA 2')
            answerFromChat = chatGptService.askQuestionToChatGpt(dataFromRequest.get('answer'))
            writerService.saveStoryMessageToDb(StoryMessage, dataFromRequest.get('storyId'), 'user', answerFromChat)
            print('Odpowiedz z chatu : '+answerFromChat)
            return Response({'message': answerFromChat, 'storyId': dataFromRequest.get('storyId')}, status=status.HTTP_201_CREATED, content_type='application/json')
        except(TypeError, ValueError, OverflowError, Story.DoesNotExist):
            print('EXECPTION 1')
            return Response({'message': 'Error Exist'}, status=status.HTTP_400_BAD_REQUEST)
