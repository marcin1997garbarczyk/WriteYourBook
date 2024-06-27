from backendApp.Services.chatGptService import ChatGptService
from backendApp.models import Story, StoryMessage


class WriterService:

    def startYourOwnStory(self, serializer, userId):
        obj = Story()
        obj.language = serializer.data.get('language')
        obj.storyType = serializer.data.get('storyType')
        obj.gender = serializer.data.get('gender')
        obj.ownerId = userId
        obj.characterName = serializer.data.get('characterName')
        obj.inspiration = serializer.data.get('inspiration')
        obj.additionalPlotOutline = serializer.data.get('additionalPlotOutline')

        obj.questionToChat = self.generateStartingMessageTocHAT(obj)
        obj.save()
        return obj

    def saveStoryMessageToDb(self, storyId, role, content):
        obj = StoryMessage()
        obj.storyId = storyId
        obj.role = role
        obj.content = content
        if(role=='assistant'):
            obj.history = self.getTextFromTag(content, 'history')
            obj.decisions = self.getTextFromTag(content, 'decisions')
            obj.style = self.getTextFromTag(content, 'style')
        obj.save()
        return obj

    def updateStoryTitle(self, chatAnswer,  storyId):
        storyObj = Story.objects.get(pk=storyId)
        storyObj.storyTitle = self.getTextFromTag(chatAnswer, 'title')
        storyObj.save()

    def getTextFromTag(self, text, tag):
        if(tag not in text):
            return ''
        else:
            startTag = text.index(f'<{tag}>')
            endTag = text.index(f'</{tag}>')
            trimmedText = ''
            if(startTag > -1 and endTag > -1):
                trimmedText = text[(int(startTag) + int(len(tag)+2)): endTag]
            return trimmedText

    def generateStartingMessageTocHAT(self, obj):
        if(obj.language == 'Polish'):
            return f'Chciałbym, żebyś napisał dla mnie historie, chce żeby była dynamiczna, żebyś co strona pytał mnie o decyzję jaką podjąłbym jaką główny bohater. ' \
                               f'Historia ma być typu {obj.storyType}. ' \
                               f'Płeć głównego bohatera to {obj.gender} a jego imię to {obj.characterName}.  ' \
                               f'Historię lub książki na których masz się wzorować to {obj.inspiration}. ' \
                               f'Dodatkowe szczęgóły dotyczące opowiadania {obj.additionalPlotOutline}. ' \
                               f'Na końcu każdego rozdziału podawaj 3 opcje jakie mogę podjąć jako główny bohater i czekaj na mój wybór w odpowiedzi. ' \
                             f'Odpowiedź przygotuj w dwóch osobnych tagach w tagu <history> przygotuj treść opowiadania w formacie html, ale tutaj nie zamieszczaj jeszcze odpowiedzi' \
                             f'a w tag <decisions> przygotuj liste odpowiedzi jakie może wybrać użytkownik aby kontynuować historie w formacie listy podzielonej średnikami.' \
                             f'Tytuł opowiadania zapisz w tagu <title> i nie zamieszczaj go już w html w tagu <h1>, tam może być nazwa rozdziału, który będzie umieszczony w tagu <history>. ' \
                             f'Nie powtarzaj tych samych rozdziałów w odpowiedziach'
        elif(obj.language == 'English'):
            return f'I would like you to write a story for me. I want it to be dynamic, and I want you to ask me on each page what decision I would make as the main character. ' \
                             f'The story should be of the type {obj.storyType}. ' \
                             f'The gender of the main character is {obj.gender} and their name is {obj.characterName}. ' \
                             f'The story or books you should be inspired by are {obj.inspiration}. ' \
                             f'Additional details about the plot are {obj.additionalPlotOutline}. ' \
                             f'At the end of each chapter, provide 3 options that I can choose from as the main character and wait for my response. ' \
                             f'Prepare your response in two separate tags. In the <history> tag, prepare the story content in HTML format, but do not include the responses there yet. ' \
                             f'In the <decisions> tag, prepare a list of possible responses that the user can choose to continue the story, formatted as a semicolon-separated list. ' \
                             f'Save the title of the story in the <title> tag and do not include it in the HTML <h1> tag, where only the chapter name will be placed in the <history> tag. ' \
                             f'Do not repeat the same chapters in responses.'
