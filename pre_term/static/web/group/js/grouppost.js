var groupPostTitle = document.getElementById('groupPostTitle');
var groupPostText = document.getElementById('groupPostText');
var groupPostWrong = document.getElementById('groupPostWrong');
var groupPostSubmit = document.getElementById('groupPostSubmit');

groupPostSubmit.addEventListener('click', function (event) {
    if(groupPostTitle.value.length === 0){
        groupPostWrong.className = "wrongText";
        groupPostWrong.innerHTML = '请输入帖子标题';
        event.preventDefault();
    }
    else if(groupPostText.value.length < 25){
        groupPostWrong.className = "wrongText";
        groupPostWrong.innerHTML = '帖子内容不能少于25个字';
        event.preventDefault();
    }
})