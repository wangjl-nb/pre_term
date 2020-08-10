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
var score = document.getElementById('score');
var review = document.getElementById('review');
var maskbg = document.getElementById('maskbg');
var scoreButton = document.getElementById('scoreButton');
var reviewButton = document.getElementById('reviewButton');
var scoreClose = document.getElementById('scoreClose');
var reviewClose = document.getElementById('reviewClose');
var scoreNumber = document.getElementById('scoreNumber');
var reviewTitle = document.getElementById('reviewTitle');
var reviewText = document.getElementById('reviewText');
var scoreSubmit = document.getElementById('scoreSubmit');
var reviewSubmit = document.getElementById('reviewSubmit');

var scoreWrong = document.getElementById('scoreWrong');
var reviewWrong = document.getElementById('reviewWrong');


windowOn(score, scoreButton);
windowOn(review, reviewButton);
close(score, scoreClose);
close(review, reviewClose);
reviewSubmit.addEventListener('click', function (event) {
    if(reviewTitle.value.length === 0){
        reviewWrong.className = "wrongText";
        reviewWrong.innerHTML = '请输入评论标题';
        event.preventDefault();
    }
    else if(reviewText.value.length < 25){
        reviewWrong.className = "wrongText";
        reviewWrong.innerHTML = '评论内容不能少于25个字';
        event.preventDefault();
    }
});
scoreSubmit.addEventListener('click', function (event) {
    if(scoreNumber.value.length === 0 ){
        scoreWrong.className = "wrongText";
        scoreWrong.innerHTML = '请输入分数（1~10的整数，包括1和10）';
        event.preventDefault();
    }
    else if(scoreNumber < 1 || scoreNumber > 10){
        scoreWrong.className = "wrongText";
        scoreWrong.innerHTML = '请输入1~10内的数字';
        event.preventDefault();
    }
});
