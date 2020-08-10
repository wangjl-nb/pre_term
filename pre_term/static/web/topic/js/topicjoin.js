$(function () {
    $("#topicjoin").click(function () {
        $.getJSON('/web/checkuser1/', function (data) {
            console.log(data);

            if (data['status'] === 302) {
                window.open('/web/login/', target = "_self");
            }
        })

    })
});