addEventListener("load", function () {
    setTimeout(hideURLbar, 0);
}, false);

function hideURLbar() {
    window.scrollTo(0, 1);
}

var user = document.getElementById('username');
var email = document.getElementById('email');
var pwd = document.getElementById('password');
var wrong = document.getElementById('wrong');
var eyeFlag = 0;
var btn = document.getElementById('submit');
var regx = /^(?!([a-zA-Z]+|\d+)$)[a-zA-Z\d]{6,16}$/;
var emregx = /^\w{3,}(\.\w+)*@[A-z0-9]+(\.[A-z]{2,5}){1,2}$/;
var eye = document.getElementById('eye');
var pwd2 = document.getElementById('password2');
var eye2 = document.getElementById('eye2');
var eyeFlag2 = 0;

function eyeDisplay(eye, eyeFlag, pwd) {
    eye.addEventListener('click', function () {
        if (eyeFlag === 0) {
            pwd.type = 'text';
            eyeFlag = 1;
            eye.className = "glyphicon glyphicon-eye-open";
        } else {
            pwd.type = 'password';
            eyeFlag = 0;
            eye.className = "glyphicon glyphicon-eye-close";
        }
    })
}

btn.addEventListener('click', function (event) {
    if (user.value.length === 0) {
        wrong.className = "wrongText";
        wrong.innerHTML = '请输入用户名';
        wrong.style.color = 'red';
        event.preventDefault();
    } else if (email.value.match(emregx) == null) {
        wrong.className = "wrongText";
        wrong.innerHTML = '请输入正确的邮箱地址';
        wrong.style.color = 'red';
        event.preventDefault();
    } else if (pwd.value.length < 6 || pwd.value.length > 16 ||
        pwd.value.match(regx) == null) {
        wrong.className = "wrongText";
        wrong.innerHTML = '密码长度必须为6~16位，且必须包含数字和字母';
        wrong.style.color = 'red';

        event.preventDefault();
    } else if (pwd.value.toString() !== pwd2.value.toString()) {
        wrong.className = "wrongText";
        wrong.innerHTML = '两次输入的密码不一致';
        wrong.style.color = 'red';
        event.preventDefault();
    }
});

eyeDisplay(eye, eyeFlag, pwd);
eyeDisplay(eye2, eyeFlag2, pwd2);

$(function () {

    let $username = $("#username");

    let $email = $('#email');

    $username.change(function () {

        let username = $username.val().trim();

        let email = $email.val().trim();

        if (username.length) {
            //将用户名发送到服务器预校验
            $.getJSON('/web/checkuser/', {'username': username, 'email': email}, function (data) {
                console.log(data);
                let $username_info = $("#wrong");
                if (username.length > 10) {
                    $username_info.html("用户名不可以超过十个字").css("color", 'red');
                } else if (data['status'] === 200) {
                    $username_info.html("用户名可用").css("color", 'green');
                } else if (data['status'] === 901) {
                    $username_info.html("用户已存在").css("color", 'red');
                } else if (data['status'] === 902) {
                    $username_info.html("邮箱已存在").css("color", 'red');
                }

            })

        }

    });

    $email.change(function () {

        let username = $username.val().trim();

        let email = $email.val().trim();

        if (email.length) {
            //将用户名发送到服务器预校验
            $.getJSON('/web/checkuser/', {'username': username, 'email': email}, function (data) {
                console.log(data);

                let $username_info = $("#wrong");

                if (data['status'] === 200) {
                    $username_info.html("用户名可用").css("color", 'green');
                } else if (data['status'] === 901) {
                    $username_info.html("用户已存在").css("color", 'red');
                } else if (data['status'] === 902) {
                    $username_info.html("邮箱已存在").css("color", 'red');
                }

            })

        }

    })

});

function check() {

    let $username = $("#username");
    let username = $username.val().trim();

    if (!username) {
        return false;
    }

    let info_color = $("#wrong").css('color');

    console.log(info_color);

    if (info_color === 'rgb(255, 0, 0)') {
        return false;
    }

    let $password_input = $("#password");

    let password = $password_input.val().trim();

    $password_input.val(md5(password));

    return true;
}