
let storyId = 0;

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
//    let spinnerElement = document.getElementById('loaderInForm')
    let buttonElement = document.getElementById('buttonToSubmit')
    buttonElement.style.display = 'none'
//    spinnerElement.style.display = 'block'

    let formClass = document.querySelector('.formClass')

    let historyClass = document.querySelector('.historyBody')
    formClass.classList.add('fade-out');
    setTimeout(()=> {
        formClass.style.display = 'none';
        historyClass.style.display = 'block';
        showLoader();
    },2000)
    let htmlObject = await callToApi();
    storyId = htmlObject.storyId;
    hideLoader()

    window.location.href=`/story/${storyId}`
}

function showLoader() {
    let loader = document.querySelector('.loader')
    loader.style.display = 'block'
}

function hideLoader() {
    let loader = document.querySelector('.loader')
    loader.style.display = 'none'
}

async function getMockForHttp() {
    let objToReturn = {'storyId': 31}
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
    let objToReturn = {'storyId': apiCallParsedResponse.storyId}
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

//let alreadyInited = false;
//if(!alreadyInited) {
//    alreadyInited = init();
//}





