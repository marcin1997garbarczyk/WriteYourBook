from backendApp.Services.chatGptService import ChatGptService



class WriterService:

    # def __init__(self):
        # self.chatGptService = ChatGptService()

    def startYourOwnStory(self, storyModel, serializer):
        print('hehehehehe')
        obj = storyModel()
        obj.storyType = serializer.data.get('storyType')
        obj.gender = serializer.data.get('gender')
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
                             f'a w tag <decisions> przygotuj liste odpowiedzi jakie może wybrać użytkownik aby kontynuować historie w formacie listy podzielonej przecinkami.' \
                             f'Nie powtarzaj tych samych rozdziałów w odpowiedziach'
        print(f'OBJ QUESTION CHAT {obj.questionToChat}')
        obj.save()
        print(f'Save {obj.pk}')
        return obj

    def saveStoryMessageToDb(self, storyMessageModel, storyId, role, content):
        obj = storyMessageModel()
        obj.storyId = storyId
        obj.role = role
        obj.content = content
        obj.save()
