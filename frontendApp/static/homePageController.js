
let storyId = 0;

async function init() {
}


async function cleanBackgroundImage() {
    const backgroundContainer = document.querySelector('.containerForBody');
    backgroundContainer.style.backgroundImage = '';
    setTimeout(() => {
        backgroundContainer.classList.remove('fade-in');
    }, 1);
}


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
    },1000);
}

async function resetBackground() {
    const backgroundContainer = document.querySelector('.containerForBody');
    await setTimeout(() => {
        backgroundContainer.classList.remove('fade-in');
        backgroundContainer.classList.add('fade-out');
    }, 1);
}

async function changeStoryType() {
    let storyType =  $('#storyTypeInput').val();
    let imageUrl = 'basic';
    imageUrl = `"/static/images/background_${storyType}.png"`;

    await changeBackground(imageUrl)
}

async function submitForm() {
    let spinnerElement = document.getElementById('loaderInForm')
    let buttonElement = document.getElementById('buttonToSubmit')
    buttonElement.style.display = 'none'
    spinnerElement.style.display = 'block'

    let formClass = document.querySelector('.formClass')

    let historyClass = document.querySelector('.historyBody')
    formClass.classList.add('fade-out');
    setTimeout(()=> {
        formClass.style.display = 'none';
        historyClass.style.display = 'block';
    },2000)

    let htmlObject = await callToApi();

//    let htmlObject = await getMockForHttp()
    let htmlResponse = htmlObject.message;
    storyId = htmlObject.storyId;
    injectHtmlWithAnswer(htmlResponse)
    setTimeout(() => {
        historyClass.classList.add('fade-in-container')
    }, 2000)

    spinnerElement.style.display = 'none'
}

function injectHtmlWithAnswer(htmlResponse) {

    let historyClass = document.querySelector('.historyBody')

    let style  = htmlResponse.substring(htmlResponse.indexOf('<style>'), htmlResponse.indexOf('</style>')+8);
    let historyBlock = htmlResponse.substring(htmlResponse.indexOf('<history>')+9, htmlResponse.indexOf('</history>'))
    let decisionBlockForHtml = '<div class="decisionBlock" style="display: flex;flex-grow: inherit;flex-direction: column;">';
    let decisionBlock = htmlResponse.substring(htmlResponse.indexOf('<decisions>')+12, htmlResponse.indexOf('</decisions>'))
    let optionsForUser = decisionBlock.split(',')
    optionsForUser.forEach(option => {
        if(option.charAt(0) == ' ') option = option.slice(1);
        option = option.charAt(0).toUpperCase() + option.slice(1);
        let idForButton = option.replaceAll(' ', '_');
        let newButton = `<button class="btn btn-secondary buttonForDecision" id=${idForButton} onclick="selectAnswerToWriter(event)">${option}</button>&nbsp;`;
        decisionBlockForHtml+=newButton;
    })
    decisionBlockForHtml += '</div>'

    let displayForHtml = style+historyBlock+decisionBlockForHtml;
    debugger;
    displayForHtml = displayForHtml.replaceAll(historyClass.innerHTML, '')
    debugger;
    historyClass.innerHTML +=  style + displayForHtml;
    historyClass.outerHtml += style + displayForHtml;
    historyClass.html += style + displayForHtml;
}

async function selectAnswerToWriter(event) {
    let textFromButton = event.currentTarget.textContent;
    let idForSelectedButton = event.currentTarget.id;
    let selectedButton = document.querySelector(`#${idForSelectedButton}`);
    selectedButton.style = 'background-color: #a75c5c'

    document.querySelectorAll('.buttonForDecision').forEach(button => {
        button.disabled = true;
    })
    askObject = {'storyId': storyId, 'answer': textFromButton}

    let htmlObject = await callToApiWithAnswer(askObject);
//    let htmlObject = await getMockForAnswerHttp(askObject)
    debugger;
    let htmlResponse = htmlObject.message;
    storyId = htmlObject.storyId;
    debugger
    injectHtmlWithAnswer(htmlResponse)
    debugger;

}

async function getMockForAnswerHttp(askObject) {
    let text ='<style> body { font-family: Arial, sans-serif; } .chapter { margin-bottom: 20px; } .chapter-header { font-size: 24px; font-weight: bold; } .chapter-content { font-size: 18px; margin-top: 10px; } </style> <history> <div class="chapter"> <div class="chapter-header">Rozdział 1: Początek Wyprawy</div> <div class="chapter-content"> W mrocznej krainie Elendir, gdzie lasy kryły tajemnice, a góry strzegły swych skarbów przed niepowołanymi oczami, żył Marcin – młody, odważny chłopak z tajemniczą przeszłością. Marcin zawsze czuł, że jest coś więcej, coś poza codziennym życiem, co czeka na niego w świecie magii i mroku. Pewnego dnia, podczas zwykłego spaceru po lesie, Marcin natknął się na stary, zapomniany trakt. Wśród zarośli znalazł starą mapę, która wydawała się wskazywać drogę do legendarnej "Światła Przyszłości" – artefaktu, który mógł zmienić losy całego świata. Wiedział, że to jest jego moment. Zebrał się na odwagę i ruszył w kierunku nieznanego. Po kilku godzinach marszu dotarł do rozwidlenia drogi – jedna ścieżka prowadziła w głąb gęstego, ponurego lasu, druga w kierunku wysokich, śnieżnych szczytów. Marcin stanął przed decyzją, która mogła zaważyć na całej jego wyprawie. </div> </div> <div class="chapter"> <div class="chapter-header">Rozdział 2: Tajemnice Lasu</div> <div class="chapter-content"> Marcin, kierowany instynktem i ciekawością, wszedł w głąb ponurego lasu. Powietrze tu było ciężkie, przesycone wilgocią i zapachem mchu. Słońce ledwo przedzierało się przez gęste korony drzew, tworząc dziwaczne cienie na ziemi. Wędrując coraz głębiej, Marcin usłyszał dziwne szepty i niepokojące dźwięki. Przyśpieszył krok, próbując nie dać się złapać przez wzbierający niepokój. Nagle, tuż przed nim, ukazał się starożytny dąb o pniu tak szerokim, że mógłby schować za nim cały dom. W jego korzeniach zobaczył maleńką, błyszczącą fiolkę z niebieskim płynem oraz zakurzoną księgę z runami, której języka nie znał. W chwili, gdy Marcin sięgnął po fiolkę, usłyszał za sobą cichy szelest. Obracając się, zobaczył wysoką postać odzianą w ciemny płaszcz. Tajemnicza osoba miała na sobie kaptur, który skutecznie ukrywał jej twarz. Głos, który wydobył się spod kaptura, brzmiał jak mieszanina szeptów i grzmotów. "Czy wiesz, co trzymasz w dłoniach, przybyszu?" – zapytał nieznajomy. "Ten las skrywa więcej tajemnic, niż potrafisz sobie wyobrazić." Marcin musiał szybko zdecydować, co powinien zrobić. </div> </div> </history> <decisions> zapytać nieznajomego o jego tożsamość i intencje, uciec z fiolką i księgą, oddać znaleziska tajemniczemu nieznajomemu </decisions>'
    let objToReturn = {'message':text, 'storyId': 25}
    await new Promise(r => setTimeout(r, 2000));
    return objToReturn;
}

async function getMockForHttp() {
//    let text =  '<!DOCTYPE html><html lang="pl"><head>    <meta charset="UTF-8">    <title>Przygody Marcina</title></head><body>    <h1>Przygody Marcina</h1>    <h2>Rozdział 1: Tajemnicza Przepowiednia</h2>    <p>W królestwie Eldaris, gdzie magia i miecz współistniały od wieków, mieszkał młody wojownik imieniem Marcin. Pewnej nocy, gdy wracał z patrolu, spotkał tajemniczego starca ubranego w ciemne szaty. Starzec wręczył mu starożytną mapę i wyszeptał: "Marcinie, ty jesteś jedyną nadzieją Eldaris. Musisz odnaleźć Zaginioną Świątynię i powstrzymać Króla Cieni."</p>    <p>Marcin, choć pełen wątpliwości, poczuł ciężar odpowiedzialności. Wiedziano, że Król Cieni gromadzi siły i Eldaris potrzebowała bohatera. Wiedział, że musi podjąć natychmiastową decyzję.</p>    <h3>Wybierz swoją decyzję:</h3>    <ol>        <li>Wyruszyć samotnie na niebezpieczną misję, polegając na swojej odwadze i determinacji.</li>        <li>Skontaktować się z Elionem, swoim przyjacielem i potężnym magiem, prosząc go o pomoc.</li>        <li>Udać się do zamku króla Alarica i poprosić o wsparcie jego rycerzy w tej trudnej wyprawie.</li>    </ol>    <p>Proszę, wybierz jedną z opcji, aby kontynuować historię!</p></body></html>';
    let text =' <style>  body {    font-family: Arial, sans-serif;  }  .chapter {    margin-bottom: 20px;  }  .chapter-header {    font-size: 24px;    font-weight: bold;  }  .chapter-content {    font-size: 18px;    margin-top: 10px;  }</style><history>  <div class="chapter">    <div class="chapter-header">Rozdział 1: Początek Wyprawy</div>    <div class="chapter-content">      W mrocznej krainie Elendir, gdzie lasy kryły tajemnice, a góry strzegły swych skarbów przed niepowołanymi oczami, żył Marcin – młody, odważny chłopak z tajemniczą przeszłością. Marcin zawsze czuł, że jest coś więcej, coś poza codziennym życiem, co czeka na niego w świecie magii i mroku.      Pewnego dnia, podczas zwykłego spaceru po lesie, Marcin natknął się na stary, zapomniany trakt. Wśród zarośli znalazł starą mapę, która wydawała się wskazywać drogę do legendarnej "Światła Przyszłości" – artefaktu, który mógł zmienić losy całego świata.      Wiedział, że to jest jego moment. Zebrał się na odwagę i ruszył w kierunku nieznanego. Po kilku godzinach marszu dotarł do rozwidlenia drogi – jedna ścieżka prowadziła w głąb gęstego, ponurego lasu, druga w kierunku wysokich, śnieżnych szczytów.      Marcin stanął przed decyzją, która mogła zaważyć na całej jego wyprawie.    </div>  </div></history><decisions>  iść w głąb ponurego lasu, wspiąć się na śnieżne szczyty, wrócić do domu po więcej zapasów</decisions>'

    let objToReturn = {'message':text, 'storyId': 25}
    await new Promise(r => setTimeout(r, 2000));

    return objToReturn;
}

async function callToApi() {
    let storySummary = {
        storyType: $('#storyTypeInput').val(),
        gender: $('#genderCharacterInput').val(),
        characterName: $('#nameOfCharacter').val(),
        inspiration: $('#inspirationForStory').val(),
        additionalPlotOutline: $('#additionalPlotOutline').val(),
    }

    let apiCallResponse = await fetch("/api/submit_story_form", {
          method: "POST",
          body: JSON.stringify(storySummary),
            credentials: "same-origin",
            headers: {
              "X-CSRFToken": getCookie("csrftoken"),
              "Accept": "application/json",
              'Content-Type': 'application/json'
            },
        })

    let apiCallParsedResponse = await apiCallResponse.json();

    let formElement = document.querySelector('.formClass');
    formElement.style.display="none"

    let infoMessage = document.getElementById('infoAfterSave');
    apiCallParsedResponse.message = apiCallParsedResponse.message.replaceAll('```html','````');
    debugger;
    let htmlResponse = apiCallParsedResponse.message.split('```')[0];
    debugger;
    if(!htmlResponse.includes('<history>')) {
        htmlResponse = apiCallParsedResponse.message.split('```')[1];
    }
    debugger;
    let objToReturn = {'message':htmlResponse, 'storyId': apiCallParsedResponse.storyId}
    return objToReturn;
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

    debugger;
    let apiCallParsedResponse = await apiCallResponse.json();
    debugger;
    apiCallParsedResponse.message = apiCallParsedResponse.message.replaceAll('```html','````');
    let htmlResponse = apiCallParsedResponse.message.split('```')[0];
    if(!htmlResponse.includes('<history>')) {
        htmlResponse = apiCallParsedResponse.message.split('```')[1];
    }
    debugger;
    let objToReturn = {'message':htmlResponse, 'storyId': apiCallParsedResponse.storyId}
    debugger;
    return objToReturn;
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

let alreadyInited = false;
if(!alreadyInited) {
    alreadyInited = init();
}





