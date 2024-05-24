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
                             f'Historia ma być zwrócona w formacie html.  '
        print(f'OBJ QUESTION CHAT {obj.questionToChat}')
        obj.save()
        print(f'Save {obj.pk}')
        return obj
