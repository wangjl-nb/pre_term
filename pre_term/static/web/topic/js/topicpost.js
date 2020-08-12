var topicPostTitle = document.getElementById('topicPostTitle');
var topicPostText = document.getElementById('topicPostText');
var topicPostWrong = document.getElementById('topicPostWrong');
var topicPostSubmit = document.getElementById('topicPostSubmit');

topicPostSubmit.addEventListener('click', function (event) {
    if(topicPostTitle.value.length === 0){
        topicPostWrong.className = "wrongText";
        topicPostWrong.innerHTML = '请输入帖子标题';
        event.preventDefault();
    }
})