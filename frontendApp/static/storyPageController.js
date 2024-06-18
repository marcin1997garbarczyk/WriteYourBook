let url = window.location.pathname;
let storyId = url.substring(url.lastIndexOf('/') + 1);;

async function init() {
    let historyClass = document.querySelector('.historyBody')
    historyClass.style.display = 'block'
    await callToApi();
    await getBalanceOfCurrentUser();
    setTimeout(() => {
        historyClass.classList.add('fade-in-container')
        window.scrollTo(0, document.body.scrollHeight);
    }, 500)
}


async function callToApi() {
    let apiCallResponse = await fetch(`/api/get_story_details/${storyId}`, {
        method: "GET",
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            'Content-Type': 'application/json'
        },
    })
    let apiCallParsedResponse = await apiCallResponse.json();

    let storyMessages = apiCallParsedResponse.storyMessages;
    let storiesElement = document.querySelector('.historyBody')
    let mainStory = apiCallParsedResponse.mainStory[0];
    let titleStoryElement = document.querySelector('.titleStory')
    titleStoryElement.textContent = mainStory.storyTitle
    changeStoryType(mainStory.storyType)
    storyMessages.forEach((storyMessage, index, storyMessagesArray) => {
        if (index == 0) {

        } else {

            if (storyMessage.role == 'assistant') {
                injectHtmlWithAnswer(storyMessage);
                if (index !== storyMessagesArray.length - 1) {
                    disableAllButtons();
                    hideNotSelectedButtons();
                }
            } else if (storyMessage.role == 'user') {
                colorButtonForPreviousQuestions(storyMessage)
            }
        };
    })

    //    askObject = {'storyId': storyId, 'answer': textFromButton}
}

async function getMockForAnswerHttp(askObject) {
    let text = '<style> body { font-family: Arial, sans-serif; } .chapter { margin-bottom: 20px; } .chapter-header { font-size: 24px; font-weight: bold; } .chapter-content { font-size: 18px; margin-top: 10px; } </style> <history> <div class="chapter"> <div class="chapter-header">Rozdział 1: Początek Wyprawy</div> <div class="chapter-content"> W mrocznej krainie Elendir, gdzie lasy kryły tajemnice, a góry strzegły swych skarbów przed niepowołanymi oczami, żył Marcin – młody, odważny chłopak z tajemniczą przeszłością. Marcin zawsze czuł, że jest coś więcej, coś poza codziennym życiem, co czeka na niego w świecie magii i mroku. Pewnego dnia, podczas zwykłego spaceru po lesie, Marcin natknął się na stary, zapomniany trakt. Wśród zarośli znalazł starą mapę, która wydawała się wskazywać drogę do legendarnej "Światła Przyszłości" – artefaktu, który mógł zmienić losy całego świata. Wiedział, że to jest jego moment. Zebrał się na odwagę i ruszył w kierunku nieznanego. Po kilku godzinach marszu dotarł do rozwidlenia drogi – jedna ścieżka prowadziła w głąb gęstego, ponurego lasu, druga w kierunku wysokich, śnieżnych szczytów. Marcin stanął przed decyzją, która mogła zaważyć na całej jego wyprawie. </div> </div> <div class="chapter"> <div class="chapter-header">Rozdział 2: Tajemnice Lasu</div> <div class="chapter-content"> Marcin, kierowany instynktem i ciekawością, wszedł w głąb ponurego lasu. Powietrze tu było ciężkie, przesycone wilgocią i zapachem mchu. Słońce ledwo przedzierało się przez gęste korony drzew, tworząc dziwaczne cienie na ziemi. Wędrując coraz głębiej, Marcin usłyszał dziwne szepty i niepokojące dźwięki. Przyśpieszył krok, próbując nie dać się złapać przez wzbierający niepokój. Nagle, tuż przed nim, ukazał się starożytny dąb o pniu tak szerokim, że mógłby schować za nim cały dom. W jego korzeniach zobaczył maleńką, błyszczącą fiolkę z niebieskim płynem oraz zakurzoną księgę z runami, której języka nie znał. W chwili, gdy Marcin sięgnął po fiolkę, usłyszał za sobą cichy szelest. Obracając się, zobaczył wysoką postać odzianą w ciemny płaszcz. Tajemnicza osoba miała na sobie kaptur, który skutecznie ukrywał jej twarz. Głos, który wydobył się spod kaptura, brzmiał jak mieszanina szeptów i grzmotów. "Czy wiesz, co trzymasz w dłoniach, przybyszu?" – zapytał nieznajomy. "Ten las skrywa więcej tajemnic, niż potrafisz sobie wyobrazić." Marcin musiał szybko zdecydować, co powinien zrobić. </div> </div> </history> <decisions> zapytać nieznajomego o jego tożsamość i intencje, uciec z fiolką i księgą, oddać znaleziska tajemniczemu nieznajomemu </decisions>'
    let objToReturn = {
        'message': text,
        'storyId': 25
    }
    await new Promise(r => setTimeout(r, 2000));
    return objToReturn;
}

function disableAllButtons() {
    document.querySelectorAll('.buttonForDecision').forEach(button => {
        button.disabled = true;
    })
}

function hideNotSelectedButtons() {
    document.querySelectorAll(':disabled').forEach(button => {
        if (!button.classList.contains('selectedButton')) {
            button.style.display = 'none'
        }
    })
}

function colorButtonForPreviousQuestions(storyMessage) {
    let selectedButton = querySelectorIncludesText('button', storyMessage.content);
    selectedButton.classList.add('selectedButton');
    selectedButton.style.display = 'block';
}

async function selectAnswerToWriter(event) {
    currentBalance = await getBalanceOfCurrentUser()
    if (currentBalance > 0) {
        let textFromButton = event.target.textContent;
        let selectedButton = querySelectorIncludesText('button', textFromButton)
        selectedButton.classList.add('selectedButton');

        document.querySelectorAll(':enabled').forEach(button => {
            button.disabled = true;

            if (!button.classList.contains('selectedButton')) {
                button.classList.add('fade-out');
                setTimeout(() => {
                    button.style.display = 'none';
                }, 2000)
            }
        })

        setTimeout(() => {
            window.scrollTo(0, document.body.scrollHeight);
        }, 500);
        askObject = {
            'storyId': storyId,
            'answer': textFromButton
        }
        showLoader();
        let htmlObject = await callToApiWithAnswer(askObject);
        let htmlResponse = htmlObject.message;
        storyId = htmlObject.storyId;
        injectHtmlWithAnswer(htmlResponse)
        await getBalanceOfCurrentUser()
        hideLoader();
        setTimeout(() => {
            window.scrollTo(0, document.body.scrollHeight);
        }, 500);
    } else {
        $('#myModal').modal('toggle');
        $('#myModal').modal('show');
    }
}

function showLoader() {
    let loader = document.querySelector('.loader')
    loader.classList.add('fade-out');
    loader.style.setProperty('display', 'block', 'important')
    setTimeout(() => {
        loader.classList.remove('fade-out')
        loader.classList.add('fade-in-container');
    }, 1000)
}

function hideLoader() {
    let loader = document.querySelector('.loader')
    loader.classList.add('fade-out');
    loader.style.setProperty('display', 'none', 'important')
}

async function callToApiWithAnswer(askObject) {

    let apiCallResponse = await fetch("/api/submit_answer_from_user", {
        method: "POST",
        body: JSON.stringify(askObject),
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            'Content-Type': 'application/json'
        },
    })


    let apiCallParsedResponse = await apiCallResponse.json();
    let objToReturn = {
        'message': apiCallParsedResponse.message,
        'storyId': apiCallParsedResponse.storyId
    }

    return objToReturn;
}

function injectHtmlWithAnswer(htmlResponse) {

    let historyClass = document.querySelector('.historyBody')

    let style = '';
    if (htmlResponse.style) {
        style = htmlResponse.style;
    }
    let historyBlock = htmlResponse.history;
    let decisionBlockForHtml = '<div class="decisionBlock" style="display: flex;flex-grow: inherit;flex-direction: column; margin-top:20px">';
    let decisionBlock = htmlResponse.decisions
    let optionsForUser = decisionBlock.split(';')
    optionsForUser.forEach(option => {
        if (option.startsWith('\n')) {
            option = option.replace('\n', '')
        }
        if (option.charAt(0) == ' ') option = option.slice(1);
        if (option.charAt(1) == ' ') option = option.slice(1);
        let trimmedVersionOfOption = option.replaceAll('\n', '').trim()
        if (trimmedVersionOfOption) {
            option = option.charAt(0).toUpperCase() + option.slice(1);
            let idForButton = option.replaceAll(' ', '_');
            let newButton = `<button class="btn btn-secondary buttonForDecision" id=${idForButton} onclick="selectAnswerToWriter(event)">${option}</button>&nbsp;`;
            decisionBlockForHtml += newButton;
        }
    })
    decisionBlockForHtml += '</div>'

    let displayForHtml = style + historyBlock + decisionBlockForHtml;
    displayForHtml = displayForHtml.replaceAll(historyClass.innerHTML, '')
    historyClass.innerHTML += style + displayForHtml;
    historyClass.outerHtml += style + displayForHtml;
    historyClass.html += style + displayForHtml;
}

function querySelectorIncludesText(selector, text) {
    return Array.from(document.querySelectorAll(selector))
        .find(el => el.textContent.includes(text));
}

function buildBootstrapCard(story) {
    return `<div class="card" style="width: 25rem; margin:10px">
        <div class="card-body" >
            <h5 class="card-title" style="text-align: center">Story ${story.id}</h5>
            <h6 class="card-subtitle mb-2 text-muted" style="text-align: center">Type: ${story.storyType}</h6>
            <p class="card-text" style="text-align: center">Character: ${story.characterName}</p>
        </div>
    </div>`
}


async function cleanBackgroundImage() {
    const backgroundContainer = document.querySelector('.containerForBody');
    backgroundContainer.style.backgroundImage = '';
    setTimeout(() => {
        backgroundContainer.classList.remove('fade-in');
    }, 1);
}

//async function changeBackground(imageUrl) {
//    const backgroundContainer = document.querySelector('.containerForBody');
//    backgroundContainer.style.backgroundImage = `url(${imageUrl})`;
//}

async function changeBackground(imageUrl) {
    const backgroundContainer = document.querySelector('.containerForBody');

    backgroundContainer.classList.remove('fade-in');
    backgroundContainer.classList.add('fade-out');
    setTimeout(() => {
        backgroundContainer.style.backgroundImage = `url(${imageUrl})`;
        setTimeout(() => {
            backgroundContainer.classList.remove('fade-out');
            backgroundContainer.classList.add('fade-in');
        }, 10);
    }, 1000);
}

async function resetBackground() {
    const backgroundContainer = document.querySelector('.containerForBody');
    await setTimeout(() => {
        backgroundContainer.classList.remove('fade-in');
        backgroundContainer.classList.add('fade-out');
    }, 1);
}

async function changeStoryType(storyType) {
    let imageUrl = 'basic';
    imageUrl = `"/static/images/background_${storyType}.png"`;

    await changeBackground(imageUrl)
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

async function getBalanceOfCurrentUser() {
    let apiCallResponse = await fetch("/api/get_balance", {
        method: "GET",
        credentials: "same-origin",
        headers: {
            "X-CSRFToken": getCookie("csrftoken"),
            "Accept": "application/json",
            'Content-Type': 'application/json'
        },
    })

    let apiCallParsedResponse = await apiCallResponse.json();
    document.querySelector('#balance_value').textContent = apiCallParsedResponse.userWalletBalance;
    return apiCallParsedResponse.userWalletBalance;
}

let alreadyInited = false;
if (!alreadyInited) {
    alreadyInited = init();
}