from backendApp.Services.chatGptService import ChatGptService
from backendApp.models import Story, StoryMessage


class WriterService:

    # def __init__(self):
        # self.chatGptService = ChatGptService()

    def startYourOwnStory(self, serializer, userId):
        obj = Story()
        obj.storyType = serializer.data.get('storyType')
        obj.gender = serializer.data.get('gender')
        obj.ownerId = userId
        obj.characterName = serializer.data.get('characterName')
        obj.inspiration = serializer.data.get('inspiration')
        obj.additionalPlotOutline = serializer.data.get('additionalPlotOutline')
        obj.questionToChat = f'Chciałbym, żebyś napisał dla mnie historie, chce żeby była dynamiczna, żebyś co strona pytał mnie o decyzję jaką podjąłbym jaką główny bohater. ' \
                               f'Historia ma być typu {obj.storyType}. ' \
                               f'Płeć głównego bohatera to {obj.gender} a jego imię to {obj.characterName}.  ' \
                               f'Historię lub książki na których masz się wzorować to {obj.inspiration}. ' \
                               f'Dodatkowe szczęgóły dotyczące opowiadania {obj.additionalPlotOutline}. ' \
                               f'Na końcu każdego rozdziału podawaj 3 opcje jakie mogę podjąć jako główny bohater i czekaj na mój wybór w odpowiedzi. ' \
                             f'Odpowiedź przygotuj w dwóch osobnych tagach w tagu <history> przygotuj treść opowiadania w formacie html, ale tutaj nie zamieszczaj jeszcze odpowiedzi' \
                             f'a w tag <decisions> przygotuj liste odpowiedzi jakie może wybrać użytkownik aby kontynuować historie w formacie listy podzielonej średnikami.' \
                             f'Tytuł opowiadania zapisz w tagu <title> i nie zamieszczaj go już w html w tagu <h1>, tam może być nazwa rozdziału, który będzie umieszczony w tagu <history>. ' \
                             f'Nie powtarzaj tych samych rozdziałów w odpowiedziach'
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
