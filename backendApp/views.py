from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .Services.chatGptService import ChatGptService
from .Services.writerService import WriterService
from .models import Story, StoryMessage
from .serializers import StoryFormSerializer
from django.forms.models import model_to_dict
from django.core.serializers import serialize

writerService = WriterService()
chatGptService = ChatGptService()

class SubmitStoryFormView(APIView):
    def post(self, request, format=None):
        serializer = StoryFormSerializer(data=request.data)

        if(serializer.is_valid()):
            try:
                newStoryObj = writerService.startYourOwnStory(Story, serializer)
                writerService.saveStoryMessageToDb(StoryMessage, newStoryObj.pk, 'user', newStoryObj.questionToChat)

                answerFromChat = chatGptService.askQuestionToChatGpt(newStoryObj.questionToChat)


                writerService.saveStoryMessageToDb(StoryMessage, newStoryObj.pk, 'assistant', answerFromChat)

                writerService.updateStoryTitle(Story, answerFromChat, newStoryObj.pk)
                print('BACKEND ZRZUCA')
                return Response({'storyId': newStoryObj.pk}, status=status.HTTP_201_CREATED, content_type='application/json')
            except(TypeError, ValueError, OverflowError, Story.DoesNotExist):
                return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            print('EXECPTION')
            return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class SubmitAnswerFromUserView(APIView):
    def post(self, request, format=None):
        print('HEHEHE')
        dataFromRequest = request.data
        print(f'data from request {dataFromRequest}')

        # try:
        chatGptService.injectStoryOfTalkWithRobot(StoryMessage, dataFromRequest.get('storyId'))
        writerService.saveStoryMessageToDb(StoryMessage, dataFromRequest.get('storyId'), 'user', dataFromRequest.get('answer'))
        print('NIMA 1')
        for message in chatGptService.chatMessages:
            print(f' message from chat {message}')
        print('NIMA 2')
        answerFromChat = chatGptService.askQuestionToChatGpt(dataFromRequest.get('answer'))
        newStoryMessage = writerService.saveStoryMessageToDb(StoryMessage, dataFromRequest.get('storyId'), 'assistant', answerFromChat)
        # print('Odpowiedz z chatu : '+newStoryMessage)
        return Response({'message': model_to_dict(newStoryMessage), 'storyId': dataFromRequest.get('storyId')}, status=status.HTTP_201_CREATED, content_type='application/json')
        # except(TypeError, ValueError, OverflowError, Story.DoesNotExist):
        #     print('EXECPTION 1')
        #     return Response({'message': 'Error Exist'}, status=status.HTTP_400_BAD_REQUEST)



class GetMyStoriesView(APIView):
    def get(self, request, format=None):
        # collectionOfStoryMessages = StoryMessage.objects.all().values()
        collectionOfStory = Story.objects.all().values()
        # print(collectionOfStoryMessages)
        # print(collectionOfStory)
        return Response({'stories': collectionOfStory},
                        status=status.HTTP_200_OK, content_type='application/json')

class GetStoryDetails(APIView):
    def get(self, request, id, format=None):
        # collectionOfStoryMessages = StoryMessage.objects.all().values()
        collectionOfStory = StoryMessage.objects.filter(storyId = id).values()

        mainStory = Story.objects.filter(id=id).values()
        # print(collectionOfStoryMessages)
        # print(collectionOfStory)
        return Response({'storyMessages': collectionOfStory, 'mainStory': mainStory},
                        status=status.HTTP_200_OK, content_type='application/json')
