var eye1 = document.getElementById('eye');
var eye2 = document.getElementById('eye2');
var eye3 = document.getElementById('eye3');
var eyeFlag1 = 0;
var eyeFlag2 = 0;
var eyeFlag3 = 0;
var oldpwd = document.getElementById('oldpwd');
var newpwd1 = document.getElementById('newpwd1');
var newpwd2 = document.getElementById('newpwd2');
var btn = document.getElementById('submit');
var regx = /^(?!([a-zA-Z]+|\d+)$)[a-zA-Z\d]{6,16}$/;
var changepwdwrong = document.getElementById('changepwdwrong');

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

eyeDisplay(eye1, eyeFlag1, oldpwd);
eyeDisplay(eye2, eyeFlag2, newpwd1);
eyeDisplay(eye3, eyeFlag3, newpwd2);

btn.addEventListener('click', function (event) {
    if (oldpwd.value === 0) {
        changepwdwrong.className = "wrongText";
        changepwdwrong.innerHTML = '请输入原密码';
        event.preventDefault();
    } else if (!newpwd1.matches(regx)) {
        changepwdwrong.className = "wrongText";
        changepwdwrong.innerHTML = '密码长度必须为6~16位，且必须包含数字和字母';
        event.preventDefault();
    } else if (newpwd1.value.toString() !== newpwd2.value.toString()) {
        changepwdwrong.className = "wrongText";
        changepwdwrong.innerHTML = '两次输入的密码不一致';
        event.preventDefault();
    }
});
$(function () {
    let $newpwd1 = $("#newpwd1");
    $newpwd1.change(function () {
        let newpwd = $newpwd1.val().trim();
        let $newpwd_info = $("#changewrong");
        if (newpwd.length) {
            console.log(newpwd.length);
            if(!strCheck(newpwd)){
                $newpwd_info.html("密码长度必须为6~16位，且必须包含数字和字母").css("color", 'red');
            }else{
                $newpwd_info.html("新密码可用").css("color", 'green');
            }
        }else{
            $newpwd_info.html("密码不能为空").css("color", 'red');
        }
    });
});
function strCheck(str){
    if(str.length>=6&&str.length<=16){
        return !!/([a-zA-Z]+[0-9]+|[0-9]+[a-zA-Z])/.exec(str);
    }else{
      return false;
    }
}
function parse_data() {

    let $oldpwd = $("#oldpwd");
    let $newpwd1 = $("#newpwd1");
    let $newpwd2 = $("#newpwd2");

    let info_color = $("#changewrong").css('color');
    if (info_color === 'rgb(255, 0, 0)') {
        return false;
    }

    let oldpwd = $oldpwd.val().trim();
    let newpwd1 = $newpwd1.val().trim();
    let newpwd2 = $newpwd2.val().trim();

    $oldpwd.val(md5(oldpwd));
    $newpwd1.val(md5(newpwd1));
    $newpwd2.val(md5(newpwd2));

    return true
}