// CSRF code
function getCookie(name) {
  var cookieValue = null;
  var i = 0;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (i; i < cookies.length; i++) {
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
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}


// JQuery visibility functions

function minimizeActions(){
    let calendarDiv = $("#calendar");
    let actionsDiv = $("#actions");
    let arrowIcon = $("#arrow-icon")
    let arrowIconButton = $("#arrow-icon-button")


    // actionsDiv.toggleClass("invisible");
    // arrowIconButton.toggleClass("visible");

    calendarDiv.toggleClass("col-12 col-sm-6 col-md-8 col-lg-8 col-xl-9");
    calendarDiv.toggleClass("col-12 col-sm-12 col-md-12 col-lg-12 col-xl-12");

    arrowIcon.toggleClass("fa-chevron-down")
    arrowIcon.toggleClass("fa-chevron-right")

    actionsDiv.toggleClass("col-12 col-sm-6 col-md-4 col-lg-4 col-xl-3");
    actionsDiv.toggleClass("col-12 col-sm-12 col-md-12 col-lg-12 col-xl-12");



    //actionsDiv.toggleClass("invisible");
    //arrowIconButton.toggleClass("visible");
}