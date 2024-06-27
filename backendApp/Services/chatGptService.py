from openai import OpenAI
import config
import os
from backendApp.models import StoryMessage


class ChatGptService:
    def __init__(self):
        if(os.environ.get('CHAT_GPT_API_KEY') is not None):
            API_KEY_OPEN_AI = os.environ.get('CHAT_GPT_API_KEY')
        else:
            API_KEY_OPEN_AI = config.CHAT_GPT_API_KEY

        self.client = OpenAI(
            api_key=API_KEY_OPEN_AI
        )
        self.chatMessages = []

    def askQuestionToChatGpt(self, recognizedText):
        self.chatMessages.append({"role": 'user', "content": recognizedText})
        responseFromChat = self.sendMessageToChatGpt()
        self.chatMessages.append({"role": 'assistant', "content": responseFromChat})
        return responseFromChat

    def sendMessageToChatGpt(self):
        chat_completion = self.client.chat.completions.create(
            messages=self.chatMessages,
            model="gpt-4o",
        )
        # print(chat_completion)
        responseFromChat = chat_completion.choices[0].message.content
        return responseFromChat

    def injectStoryOfTalkWithRobot(self, someSortOfStoryId):
        print(someSortOfStoryId)
        for storyMessage in StoryMessage.objects.filter(storyId=someSortOfStoryId):
            self.chatMessages.append({"role": storyMessage.role, "content": storyMessage.content})


