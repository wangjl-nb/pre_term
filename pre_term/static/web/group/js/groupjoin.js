$(function () {
    $(".add_group").click(function () {
        // console.log('add');

        // let $add = $(this);
        // // console.log($add.attr('goodsid'));
        // let groupid = $add.attr("groupid");
        // console.log(groupid);
        $.getJSON('/web/checkuser1/', function (data) {
            console.log(data);

            if (data['status'] === 302) {
                window.open('/web/login/', target = "_self");
            }
        })
    })
});

function windowOn(window, button) {
    button.addEventListener('click', function () {
        window.style.display = 'block';
        maskbg.style.display = 'block';
    })
}
function close(window, close) {
    close.addEventListener('click', function () {
        window.style.display = 'none';
        maskbg.style.display = 'none';
    })
}
var maskbg = document.getElementById('maskbg');
var groupJoin = document.getElementById('groupJoin');
var groupJoinLink = document.getElementById('groupJoinLink');
var groupJoinClose = document.getElementById('groupJoinClose');
windowOn(groupJoin, groupJoinLink);
close(groupJoin, groupJoinClose);

// function groupcheck() {
//
//     let $username = $("#username");
//     let username = $username.val().trim();
//
//     if (!username) {
//         return false;
//     }
//
//     let info_color = $("#wrong").css('color');
//
//     console.log(info_color);
//
//     if (info_color === 'rgb(255, 0, 0)') {
//         return false;
//     }
//
//     let $password_input = $("#password");
//
//     let password = $password_input.val().trim();
//
//     $password_input.val(md5(password));
//
//     return true;
// }