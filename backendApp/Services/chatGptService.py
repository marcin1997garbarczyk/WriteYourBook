from openai import OpenAI
import config


class ChatGptService:
    def __init__(self):
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
        # chat_completion = self.client.chat.completions.create(
        #     messages=self.chatMessages,
        #     model="gpt-3.5-turbo",
        # )
        chat_completion = self.client.chat.completions.create(
            messages=self.chatMessages,
            model="gpt-4o",
        )
        # print(chat_completion)
        responseFromChat = chat_completion.choices[0].message.content
        return responseFromChat

    def injectStoryOfTalkWithRobot(self, storyMessageModel, someSortOfStoryId):
        print(someSortOfStoryId)
        for storyMessage in storyMessageModel.objects.filter(storyId=someSortOfStoryId):
            self.chatMessages.append({"role": storyMessage.role, "content": storyMessage.content})


