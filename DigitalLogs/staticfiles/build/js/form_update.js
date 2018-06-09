function on_form_change(form) {
    clone_last_line(form);
    clear_empty_lines(form);

    if (!$(form).find()) {

    }

    $.ajax({
        type: 'POST',
        url: $(form).attr('action'),
        data: $(form).serialize(),
        success: console.log,
        dataType: "json"
    });
}

function on_input_change(input) {
    const json = input.dataset.info.replace(/'/g, '"');
    const info = JSON.parse(json);

    if (info.type !== "droplist" ) {
        input.type = info.type;
    }

    if (input.type === "number" && (input.value * 1 < info.min_normal || input.value * 1 > info.max_normal)) {
        $(input).addClass('red').removeClass('black');
    } else {
        $(input).addClass('black').removeClass('red')
    }

    if (info.type === "droplist" ) {
        $(input).attr('list', 'caplist')
        $(input).add('datalist')
    }

    $(input).attr('placeholder', info.units);
    $(input).attr('title', info.units);
}


function line_is_empty(tr_line) {
    let filled = 0;
    tr_line.find('input').each(function () {
        if (this.value.trim() !== "") {
            filled++;
        }
    });

    return filled === 0;
}


function clone_last_line(form) {

    const table = $(form).find("table");
    const last_line = table.find(".indexed-line:last");

    if (!line_is_empty(last_line)) {
        let new_last_line = last_line.clone();
        new_last_line.find("input").val("");
        new_last_line.find(".index-input").val(last_line.find(".index-input").val()*1 + 1);
        table.append(new_last_line);
    }
}


function clear_empty_lines(form) {
    const table = $(form).find("table");

    let last_line = null;
    $(table.find(".indexed-line").get().reverse()).each(function (index) {
        if (line_is_empty($(this))) {
            if (last_line) {
                last_line.remove();
            }
            last_line = this;
        } else {
            return false;
        }
    });
}


$(document).ready(function () {
    document.querySelectorAll(".general-value").forEach(input => {
        on_input_change(input);
    });

    $("form").trigger("input")

    String.prototype.trim = function () {
        return this.replace(/^\s*/, "").replace(/\s*$/, "");
    }
})