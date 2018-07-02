function validate(d, m, y){

        $.ajax({
            type: "POST",
            url: "/days_by_month/validate/"+y+"/"+m+"/"+d,
            data: {
                "spent" : $("#id_spent"+m+d).val()
            },
            dataType: 'json',
            beforeSend: function(xhr, settings) {
              if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
              }
            },
            success: function (data) {
              let elem =  $("#id_spent"+m+d);
              if (!data.validate) {
                if(elem.hasClass("is-valid"))
                    elem.removeClass("is-valid");

                elem.addClass("is-invalid")
              }else{
                if(elem.hasClass("is-invalid"))
                    elem.removeClass("is-invalid");

                elem.addClass("is-valid");
              }
              let group = $("#errors"+m+d);
              group.empty();
            },
            error: function (data) {
              let elem =  $("#id_spent"+m+d);
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
              let group = $("#errors"+m+d);
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


function selectMonth(m, mini){
    let dropdown_item = $("#dropdown-item"+m);
    let dropdownMenu = $("#dropdownMenu");
    let elem, tab;

    dropdown_item.parent()[0].childNodes.forEach(function(e, c){
        e = $(e);
        if (e.hasClass("active"))
            elem = e;
    });
    //console.log(dropdownMenu);
    dropdownMenu.text(mini);

    elem.removeClass("active");
    dropdown_item.toggleClass("active");
    //console.log(dropdown_item);
    let nav = $("#nav-"+m);
    nav.parent()[0].childNodes.forEach(function(e, c){
        e = $(e);
        if (e.hasClass("active"))
            tab = e;
    });
    tab.removeClass("show active");
    nav.addClass("show active");


}
