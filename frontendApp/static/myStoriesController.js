
async function init() {
    console.log('@@@')
    await callToApi();
}

function injectHtmlWithAnswer(htmlResponse) {

    let historyClass = document.querySelector('.historyBody')

    let style  = htmlResponse.substring(htmlResponse.indexOf('<style>'), htmlResponse.indexOf('</style>')+8);

    let displayForHtml = style+historyBlock+decisionBlockForHtml;
    displayForHtml = displayForHtml.replaceAll(historyClass.innerHTML, '')

    historyClass.innerHTML +=  style + displayForHtml;
    historyClass.outerHtml += style + displayForHtml;
    historyClass.html += style + displayForHtml;
}


async function callToApi() {
    let storySummary = {}

    debugger;
    let apiCallResponse = await fetch("/api/get_my_stories", {
          method: "GET",
        credentials: "same-origin",
        headers: {
          "X-CSRFToken": getCookie("csrftoken"),
          "Accept": "application/json",
          'Content-Type': 'application/json'
        },
        })
    debugger;
    let apiCallParsedResponse = await apiCallResponse.json();
    let stories = apiCallParsedResponse.stories;
    let storiesElement = document.querySelector('.myStories')
    stories.forEach(story => {
        let storyCard = buildBootstrapCard(story);
        storiesElement.html += storyCard;
        storiesElement.innerHTML += storyCard;
        storiesElement.outerHtml += storyCard;
    })
}


function buildBootstrapCard(story) {
    return `<div class="card" style="margin:10px; width:30%;" >
        <div class="card-body" >
            <div class="cardText" style=' height:17vh'>
            <h5 class="card-title" style="text-align: center">Title: ${story.storyTitle}</h5>
            <h6 class="card-subtitle mb-2 text-muted" style="text-align: center">Type: ${story.storyType}</h6>
            <p class="card-text" style="text-align: center">Main character: ${story.characterName}</p>
            <p class="card-text" style="text-align: center">Inspiration: ${story.inspiration}</p>
            </div>
            <button class="card-text btn btn-secondary buttonForDecision"  style="text-align: center; width:100%" id=${story.id} onclick="openStory(event)">Open story</button>
        </div>
    </div>`
}

function openStory(event) {
    debugger
    window.location.href=`/story/${event.currentTarget.id}`
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





