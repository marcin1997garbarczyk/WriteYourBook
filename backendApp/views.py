from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .Services.chatGptService import ChatGptService
from .Services.writerService import WriterService
from .Services.walletService import WalletService
from .models import Story, StoryMessage, UserWallet
from .serializers import StoryFormSerializer
from django.forms.models import model_to_dict

writerService = WriterService()
chatGptService = ChatGptService()
walletService = WalletService()

class create_story(APIView):
    def post(self, request, format=None):
        serializer = StoryFormSerializer(data=request.data)
        print('19 hehe')
        isEnoughCoins = walletService.checkBalanceOnCurrentWallet(request.user.id)
        if(isEnoughCoins == False):
            return Response({'message': 'Not enough coins'}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
        else:
            if(serializer.is_valid()):
                try:
                    newStoryObj = writerService.startYourOwnStory(serializer, request.user.id)
                    writerService.saveStoryMessageToDb(newStoryObj.pk, 'user', newStoryObj.questionToChat)
                    answerFromChat = chatGptService.askQuestionToChatGpt(newStoryObj.questionToChat)
                    writerService.saveStoryMessageToDb(newStoryObj.pk, 'assistant', answerFromChat)
                    writerService.updateStoryTitle(answerFromChat, newStoryObj.pk)
                    walletService.reduceCoinInCurrentWallet(request.user.id)
                    return Response({'storyId': newStoryObj.pk}, status=status.HTTP_201_CREATED, content_type='application/json')
                except(TypeError, ValueError, OverflowError, Story.DoesNotExist):
                    return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class submit_answer(APIView):
    def post(self, request, format=None):
        dataFromRequest = request.data

        isEnoughCoins = walletService.checkBalanceOnCurrentWallet(request.user.id)
        if(isEnoughCoins == False):
            return Response({'message': 'Not enough coins'}, status=status.HTTP_400_BAD_REQUEST, content_type='application/json')
        else:
            chatGptService.injectStoryOfTalkWithRobot(dataFromRequest.get('storyId'))
            writerService.saveStoryMessageToDb(dataFromRequest.get('storyId'), 'user', dataFromRequest.get('answer'))

            answerFromChat = chatGptService.askQuestionToChatGpt(dataFromRequest.get('answer'))
            newStoryMessage = writerService.saveStoryMessageToDb(dataFromRequest.get('storyId'), 'assistant', answerFromChat)
            walletService.reduceCoinInCurrentWallet(request.user.id)
            return Response({'message': model_to_dict(newStoryMessage), 'storyId': dataFromRequest.get('storyId')}, status=status.HTTP_201_CREATED, content_type='application/json')


class get_my_stories(APIView):
    def get(self, request, format=None):
        collectionOfStory = Story.objects.filter(ownerId = request.user.id).values()
        return Response({'stories': collectionOfStory},
                        status=status.HTTP_200_OK, content_type='application/json')

class get_story_details(APIView):
    def get(self, request, id, format=None):
        collectionOfStory = StoryMessage.objects.filter(storyId = id).values()
        mainStory = Story.objects.filter(id=id).values()
        return Response({'storyMessages': collectionOfStory, 'mainStory': mainStory},
                        status=status.HTTP_200_OK, content_type='application/json')

class get_balance(APIView):
    def get(self, request, format=None):
        userWallet = walletService.get_current_wallet_for_user_id(request.user.id)
        return Response({'userWalletBalance': userWallet.balance}, status=status.HTTP_200_OK, content_type='application/json')
