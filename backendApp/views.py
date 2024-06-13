from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .Services.chatGptService import ChatGptService
from .Services.writerService import WriterService
from .Services.walletService import WalletService
from .models import Story, StoryMessage, UserWallet
from .serializers import StoryFormSerializer
from django.forms.models import model_to_dict
from django.core.serializers import serialize

writerService = WriterService()
chatGptService = ChatGptService()
walletService = WalletService()

class SubmitStoryFormView(APIView):
    def post(self, request, format=None):
        serializer = StoryFormSerializer(data=request.data)

        isEnoughCoins = walletService.checkBalanceOnCurrentWallet(UserWallet, request.user.id)
        if(isEnoughCoins == False):
            return Response({'message': 'Not enough coins'}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
        else:
            if(serializer.is_valid()):
                try:
                    newStoryObj = writerService.startYourOwnStory(Story, serializer)
                    writerService.saveStoryMessageToDb(StoryMessage, newStoryObj.pk, 'user', newStoryObj.questionToChat)

                    answerFromChat = chatGptService.askQuestionToChatGpt(newStoryObj.questionToChat)


                    writerService.saveStoryMessageToDb(StoryMessage, newStoryObj.pk, 'assistant', answerFromChat)

                    writerService.updateStoryTitle(Story, answerFromChat, newStoryObj.pk)
                    walletService.reduceCoinInCurrentWallet(UserWallet, request.user.id)
                    return Response({'storyId': newStoryObj.pk}, status=status.HTTP_201_CREATED, content_type='application/json')
                except(TypeError, ValueError, OverflowError, Story.DoesNotExist):
                    return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                print('EXECPTION')
                return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class SubmitAnswerFromUserView(APIView):
    def post(self, request, format=None):
        dataFromRequest = request.data

        isEnoughCoins = walletService.checkBalanceOnCurrentWallet(UserWallet, request.user.id)
        if(isEnoughCoins == False):
            return Response({'message': 'Not enough coins'}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
        else:
            chatGptService.injectStoryOfTalkWithRobot(StoryMessage, dataFromRequest.get('storyId'))
            writerService.saveStoryMessageToDb(StoryMessage, dataFromRequest.get('storyId'), 'user', dataFromRequest.get('answer'))

            answerFromChat = chatGptService.askQuestionToChatGpt(dataFromRequest.get('answer'))
            newStoryMessage = writerService.saveStoryMessageToDb(StoryMessage, dataFromRequest.get('storyId'), 'assistant', answerFromChat)
            walletService.reduceCoinInCurrentWallet(UserWallet, request.user.id)
            return Response({'message': model_to_dict(newStoryMessage), 'storyId': dataFromRequest.get('storyId')}, status=status.HTTP_201_CREATED, content_type='application/json')


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

class GetBalance(APIView):
    def get(self, request, format=None):
        userWallet = walletService.get_current_wallet_for_user_id(UserWallet, request.user.id)
        return Response({'userWalletBalance': userWallet.balance}, status=status.HTTP_200_OK, content_type='application/json')
