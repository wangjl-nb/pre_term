let tip_title = document.getElementById('tip_title');
let message = document.getElementById('message');
let tip_submit = document.getElementById('tip_submit');
let tipwrong = document.getElementById('tipwrong')

tip_submit.addEventListener('click', function (event) {
    if(tip_title.value.length === 0){
        tipwrong.className = "wrongText";
        tipwrong.innerHTML = '请输入举报标题';
        event.preventDefault();
    }
    else if(message.value.length < 15){
        tipwrong.className = "wrongText";
        tipwrong.innerHTML = '举报理由不能少于15个字';
        event.preventDefault();
    }
})
