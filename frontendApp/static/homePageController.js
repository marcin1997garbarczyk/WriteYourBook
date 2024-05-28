
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
        debugger
    }, 1);
}

async function changeStoryType() {
    let storyType =  $('#storyTypeInput').val();
    let imageUrl = 'basic';
    debugger;
    imageUrl = `"/static/images/background_${storyType}.png"`;
    debugger;

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

//    let htmlResponse = await callToApi();

    debugger;
    let htmlResponse = await getMockForHttp()


    historyClass.innerHTML = htmlResponse;
    historyClass.outerHtml = htmlResponse;
    historyClass.html = htmlResponse;

    setTimeout(() => {
        historyClass.classList.add('fade-in-container')
    }, 2000)

    spinnerElement.style.display = 'none'
}

async function getMockForHttp() {
    let text =  '<!DOCTYPE html><html lang="pl"><head>    <meta charset="UTF-8">    <title>Przygody Marcina</title></head><body>    <h1>Przygody Marcina</h1>    <h2>Rozdział 1: Tajemnicza Przepowiednia</h2>    <p>W królestwie Eldaris, gdzie magia i miecz współistniały od wieków, mieszkał młody wojownik imieniem Marcin. Pewnej nocy, gdy wracał z patrolu, spotkał tajemniczego starca ubranego w ciemne szaty. Starzec wręczył mu starożytną mapę i wyszeptał: "Marcinie, ty jesteś jedyną nadzieją Eldaris. Musisz odnaleźć Zaginioną Świątynię i powstrzymać Króla Cieni."</p>    <p>Marcin, choć pełen wątpliwości, poczuł ciężar odpowiedzialności. Wiedziano, że Król Cieni gromadzi siły i Eldaris potrzebowała bohatera. Wiedział, że musi podjąć natychmiastową decyzję.</p>    <h3>Wybierz swoją decyzję:</h3>    <ol>        <li>Wyruszyć samotnie na niebezpieczną misję, polegając na swojej odwadze i determinacji.</li>        <li>Skontaktować się z Elionem, swoim przyjacielem i potężnym magiem, prosząc go o pomoc.</li>        <li>Udać się do zamku króla Alarica i poprosić o wsparcie jego rycerzy w tej trudnej wyprawie.</li>    </ol>    <p>Proszę, wybierz jedną z opcji, aby kontynuować historię!</p></body></html>';
    await new Promise(r => setTimeout(r, 2000));
    return text;
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
    let htmlResponse = apiCallParsedResponse.message.split('```')[1];
    return htmlResponse;
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





