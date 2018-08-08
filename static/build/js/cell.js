
    function IsJsonString(str) {
        try {
            JSON.parse(str);
        } catch (e) {
            return false;
        }
        return true;
    }

class Cell {
    constructor() {

    }

    // public
    static onInput(input) {
        this.on_input_change(input);
        this.saveCell(input);
        $('#sync').hide();$('#async').show();
    }

    static onChange(input) {
        this.reformat_on_change(input);
        this.addMessage(input);
    }

    //private
    static saveCell(input) {
        let forSend = JSON.stringify({
            'cell': {
                'field_name': input.name,
                'table_name': $(input).attr('table-name'),
                'group_id': $(input).attr('journal-page'),
                'index': $(input).attr('index')
            },

            'value': input.value,
        });
        $.ajax({
            url: "/common/save_cell/",
            type: 'POST',
            contentType: 'application/json; charset=utf-8',
            data: forSend,
            success: function (json) {
                if (json && json.status) {
                }
            }
        });
    }

    static addMessage(msg) {
        let debounce = _.debounce((input) => {
            console.log("addMessage from debounce", input);

            const json = input.dataset.info.replace(/'/g, '"');
            const info = JSON.parse(json);

            if (input.type === "number" && (input.value * 1 < info.min_normal || input.value * 1 > info.max_normal) && input.value != '') {
                let forSend = JSON.stringify({
                    'cell': {
                        'field_name': input.name,
                        'table_name': $(input).attr('table-name'),
                        'group_id': $(input).attr('journal-page'),
                        'index': $(input).attr('index')
                    },

                    'message': { 'text': input.value, 'link': Cell.getLink(input), 'type': 'critical_value'}
                })
                $.ajax({
                    url: "/common/messages/add_critical/",
                    type: 'POST',
                    contentType: 'application/json; charset=utf-8',
                    data: forSend,
                    success: function (json) {
                        if (json && json.status) {
                            // console.log(json.result)
                        }
                    }
                });
            } else {

                let forSend = JSON.stringify({
                    'cell': {
                        'field_name': input.name,
                        'table_name': $(input).attr('table-name'),
                        'group_id': $(input).attr('journal-page'),
                        'index': $(input).attr('index')
                    }
                });

                $.ajax({
                    url: "/common/messages/update/",
                    type: 'POST',
                    contentType: 'application/json; charset=utf-8',
                    data: forSend,
                    success: function (json) {
                        if (json && json.status) {
                            // console.log(json.result)
                        }
                    }
                });
            }
        },
            300);

        debounce(msg)
    }



    static on_input_change(input) {
        const json = input.dataset.info.replace(/'/g, '"');
        // if field description exists
        if (IsJsonString(json)) {
          var info = JSON.parse(json)

        }else{
          // default field description
          var info = {'type': 'text'}
        }
        input.type = info.type;

        if (input.type === "number") {
            if ((input.value * 1 < info.min_normal || input.value * 1 > info.max_normal) && input.value != '') {
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
        let plant = location.pathname.split('/')[1];
        let journal_name = location.pathname.split('/')[2];
        let result = `/${plant}/${journal_name}?page_mode=view&highlight=${$(input).attr("id")}#${$(input).attr("id")}`;

        return result;
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
