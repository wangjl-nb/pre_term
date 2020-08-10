function parse_data(){
    let $password_input = $("#password");
    let password = $password_input.val().trim();
    $password_input.val(md5(password));
    return true
}
addEventListener("load", function() {
    setTimeout(hideURLbar, 0);
}, false);

function hideURLbar() {
    window.scrollTo(0, 1);
}
var	user = document.getElementById('username');
var pwd = document.getElementById('password');
var wrong = document.getElementById('wrong');
var eyeFlag = 0;
var btn = document.getElementById('submit')
var regx = /^(?!([a-zA-Z]+|\d+)$)[a-zA-Z\d]{6,16}$/;
var eye = document.getElementById('eye');
eye.addEventListener('click', function () {
    console.log("2");
    if(eyeFlag === 0){
        pwd.type = 'text';
        eyeFlag = 1;
        eye.className = "glyphicon glyphicon-eye-open";
    }
    else{
        pwd.type = 'password';
        eyeFlag = 0;
        eye.className = "glyphicon glyphicon-eye-close";
    }
});

btn.addEventListener('click', function (event) {
    if(user.value.length === 0 ){
        wrong.className = "wrongText";
        wrong.innerHTML = '请输入用户名';
        event.preventDefault();
    }
    else if(pwd.value.length < 6 || pwd.value.length > 16 ||
        pwd.value.match(regx) == null){
        wrong.className = "wrongText";
        wrong.innerHTML = '密码长度必须为6~16位，且必须包含数字和字母';
        event.preventDefault();
    }
});

