function validate(m, y){

        $.ajax({
            type: "POST",
            url: "/months_by_year/validate/"+y+"/"+m,
            data: {
                "balance" : $("#id_balance"+y+m).val()
            },
            dataType: 'json',
            beforeSend: function(xhr, settings) {
              if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
              }
            },
            success: function (data) {
              let elem =  $("#id_balance"+y+m);
              if (!data.validate) {
                if(elem.hasClass("is-valid"))
                    elem.removeClass("is-valid");

                elem.addClass("is-invalid")
              }else{
                if(elem.hasClass("is-invalid"))
                    elem.removeClass("is-invalid");

                elem.addClass("is-valid");
              }
              let group = $("#errors"+y+m);
              group.empty();
            },
            error: function (data) {
              let elem =  $("#id_balance"+y+m);
              if (!data.validate) {
                if(elem.hasClass("is-valid"))
                    elem.removeClass("is-valid");

                elem.addClass("is-invalid")
              }else{
                if(elem.hasClass("is-invalid"))
                    elem.removeClass("is-invalid");

                elem.addClass("is-valid");
              }
              data = data.responseJSON;
              let group = $("#errors"+y+m);
              group.empty();
              for (i = 0; i < data.errors.spent.length; i++) {
                let error = $(document.createElement("div"));
                error.addClass("alert alert-danger");

                let t = document.createTextNode(data.errors.spent[i]);
                error.append(t);
                group.append(error);
              }

            }
        });
}
