from backendApp.Services.chatGptService import ChatGptService

chatGptService = ChatGptService()

def writeStory():
    typeOfBook = input('Podaj typ opowiadania ')
    genderOfCharacter = input('Podaj płeć bohatera ')
    nameOfCharacter = input('Podaj nazwe bohatera ')
    basedOnBooks = input('Podaj ksiazki na których ma bazować ')
    plotSkeleton = input('Jeżeli chcesz to podaj dodatkowe szczegóły co do opowiadania ')

    # typeOfBook = 'Fantasy'
    # genderOfCharacter = 'Mezczyzna'
    # nameOfCharacter = 'Marcin'
    # basedOnBooks = 'Lotr, wiedzmin'
    # plotSkeleton = 'Nie wiem'

    starterInfoForWriter = f'Chciałbym, żebyś napisał dla mnie historie, chce żeby była dynamiczna, żebyś co strona pytał mnie o decyzję jaką podjąłbym jaką główny bohater. ' \
                           f'Historia ma być typu {typeOfBook}. ' \
                           f'Płeć głównego bohatera to {genderOfCharacter} a jego imię to {nameOfCharacter}.  ' \
                           f'Historię lub książki na których masz się wzorować to {basedOnBooks}. ' \
                           f'Dodatkowe szczęgóły dotyczące opowiadania {plotSkeleton}. ' \
                           f'Na końcu każdego rozdziału podawaj 3 opcje jakie mogę podjąć jako główny bohater i czekaj na mój wybór w odpowiedzi.' \
                           f'Historia ma być podana w formacie HTML. Do listy wyborów dodaj classe "selectionForStory" '


    print(f'Starter chat : {starterInfoForWriter}')
    responseFromChat = chatGptService.askQuestionToChatGpt(starterInfoForWriter)
    print(f'Response from chat {responseFromChat}')

    while True:
        decisionFromUser = input('')
        decisionFromUserFormalized = f'Podejmuję decyzję {decisionFromUser}'
        responseFromChat = chatGptService.askQuestionToChatGpt(decisionFromUserFormalized)
        print(responseFromChat)
