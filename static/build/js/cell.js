class Cell {
    constructor() {

    }

    // public
    static onInput(input, employee) {
        this.on_input_change(input);
        this.addResponsible(input, employee);
        this.saveCell(input);
        $('#sync').hide();$('#async').show();
    }

    static onChange(input) {
        // Journal.addMessage(input);
        // Cell.reformat_on_change(input);
    }

    //private
    static saveCell(input) {
        $.ajax({
            url: "/common/save_cell/",
            type: 'POST',
            data: {'check': true, 'id': input.id, 'value': input.value,},
            success: function (json) {
                if (json && json.status) {
                    console.log("Yep, SAVED!");
                }
            }
        });
    }

    static addResponsible(input, user) {
        $(input).siblings(".resp").attr("value", user);
    }

    static on_input_change(input) {
        const json = input.dataset.info.replace(/'/g, '"');
        const info = JSON.parse(json);

        input.type = info.type;


        if (input.type === "number") {
            if (input.value * 1 < info.min_normal || input.value * 1 > info.max_normal) {
                $(input).addClass('red').removeClass('black');
            } else {
                $(input).addClass('black').removeClass('red')
            }
        } else if (info.type === "datalist") {
            if ($(input).attr('data-pagmode') === "validate") {
                $(input).removeAttr("type");
            } else {

                $(input).removeAttr("type");
                $(input).attr('list', 'datalist');

                if ($('#datalist').length === 0) {
                    $(input).after('<datalist id="datalist"></datalist>');
                    info.options.forEach((name) => {
                        $("#datalist").append("<option>" + name + "</option>");
                    })
                }
            }
        }

        $(input).attr('placeholder', info.units);
        this.markCommented(input);
    }


    static getLink(input) {
        let plant = location.pathname.split('/')[1]
        let journal_name = location.pathname.split('/')[2]
        console.log(`/${plant}/${journal_name}?page_mode=view&highlight=${input.attr("id")}#${input.attr("id")}`);
        
        return `/${plant}/${journal_name}?page_mode=view&highlight=${input.attr("id")}#${input.attr("id")}`
    }

    static reformat_on_change(input) {
        if (input.value === "")
            return;
        if (input.type === "number") {
            input.value = +(input.value*1.0).toFixed(2);
        }
        // $(input.closest('table')).alignColumn([1, 2, 3, 4, 5], {center: '.'})
    }

    static markCommented(textarea) {
        let comment = $(textarea).parent()[0];
        let comment_notification = $(comment).siblings("i")[0];
        if ($(textarea).val()) {
            $(comment_notification).addClass("show")
        }
        else {
            $(comment_notification).removeClass("show")
        }
    }

    static resize_cell(input) {
        input.style.width = (input.value.length + 1) + 'ch';
    }
}

