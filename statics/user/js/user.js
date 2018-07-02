function validateUser(){
    let userInput =  $("#userInput");
    let errorGroup = $("#errors");
    if (userInput.val() === undefined || userInput.val() === "" || userInput.val() === null)
        return;
    $.ajax({
        type: "POST",
        url: "/validate/login/",
        data: {
            "user" : userInput.val()
        },
        dataType: 'json',
        beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        },
        success: function (data) {
            userInput.addClass("is-valid");
            userInput.removeClass("is-invalid");
            errorGroup.empty();
            $('#userInputErrors').remove();
        },
        error: function (data) {
            userInput.addClass("is-invalid");
            userInput.removeClass("is-valid");
            //console.log(data);
            data = data.responseJSON;
            errorGroup.empty();
            //Corrigir leitura dos errors
            for (i = 0; i < data.errors.length; i++) {
                let error = $(document.createElement("div"));
                error.addClass("col-12 alert alert-danger");

                let t = document.createTextNode(data.errors[i]);
                error.append(t);
                errorGroup.append(error);
              }
              $('#userInputErrors').remove();
        }
    });
}

function validatePass(){
    let passInput = $('#passInput');
    if (passInput.val() !== undefined || passInput.val() !== "" || passInput.val() !== null){
      $('#passwordInputErrors').remove();
    }
}
