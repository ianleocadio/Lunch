function validateUser(){
    $.ajax({
        type: "POST",
        url: "/accounts/validate/login/",
        data: {
            "user" : $("#userInput").val()
        },
        dataType: 'json',
        beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
        },
        success: function (data) {
            console.log("Sucesso");
            console.log(data);
        },
        error: function (data) {
            console.log("Erro");
            console.log(data);
        }
    });
}
