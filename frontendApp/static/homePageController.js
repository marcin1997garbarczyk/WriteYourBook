
async function init() {
//    let data = await callForBeachNames();
//    selectBox = $('#Selector')
//    if (data.length > 0) {
//        var output = [];
//        $.each(data, function (i, dat) {
//            output.push(`<option value=${dat}> ${dat} </option>`);
//        });
//        selectBox.html(output.join(""));
//        selectBox.selectpicker("refresh");
//        return true
//    }
//    return false
}


async function submitForm() {
    let spinnerElement = document.getElementById('loaderInForm')
    let buttonElement = document.getElementById('buttonToSubmit')
    buttonElement.style.display = 'none'
    spinnerElement.style.display = 'block'

    let storySummary = {
        storyType: $('#storyTypeInput').val(),
        gender: $('#genderCharacterInput').val(),
        characterName: $('#nameOfCharacter').val(),
        inspiration: $('#inspirationForStory').val(),
        additionalPlotOutline: $('#additionalPlotOutline').val(),
    }
    debugger

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
    debugger
    let formElement = document.getElementById('formId');
    formElement.style.display="none"

    let infoMessage = document.getElementById('infoAfterSave');
//    infoMessage.htmlContent= apiCallParsedResponse.message
//    infoMessage.textContent= apiCallParsedResponse.message

    infoMessage.innerHTML = apiCallParsedResponse.message;
    infoMessage.outerHtml = apiCallParsedResponse.message;
    infoMessage.html = apiCallParsedResponse.message;

    spinnerElement.style.display = 'none'
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