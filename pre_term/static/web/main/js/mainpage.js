let bookButton = document.getElementById('bookButton');
let movieButton = document.getElementById('movieButton');
let groupButton = document.getElementById('groupButton');
let topicButton = document.getElementById('topicButton');
let bookinput = document.getElementById('bookinput');
let movieinput = document.getElementById('movieinput');
let groupinput = document.getElementById('groupinput');
let topicinput = document.getElementById('topicinput');
let searchtype = document.getElementById('searchtype');
let booksubmit = document.getElementById('booksubmit');
let moviesubmit = document.getElementById('moviesubmit');
let groupsubmit = document.getElementById('groupsubmit');
let topicsubmit = document.getElementById('topicsubmit');

bookButton.onclick = function () {
    searchtype.innerHTML = '搜索书籍(点击其他按钮可更改搜索类别)';
    bookinput.style.display = 'inline-block';
    movieinput.style.display = 'none';
    groupinput.style.display = 'none';
    topicinput.style.display = 'none';
    booksubmit.style.display = 'inline-block';
    moviesubmit.style.display = 'none';
    groupsubmit.style.display = 'none';
    topicsubmit.style.display = 'none';
};

movieButton.onclick = function () {
    searchtype.innerHTML = '搜索影视(点击其他按钮可更改搜索类别)';
    bookinput.style.display = 'none';
    movieinput.style.display = 'inline-block';
    groupinput.style.display = 'none';
    topicinput.style.display = 'none';
    booksubmit.style.display = 'none';
    moviesubmit.style.display = 'inline-block';
    groupsubmit.style.display = 'none';
    topicsubmit.style.display = 'none';
};

groupButton.onclick = function () {
    searchtype.innerHTML = '搜索小组(点击其他按钮可更改搜索类别)';
    bookinput.style.display = 'none';
    movieinput.style.display = 'none';
    groupinput.style.display = 'inline-block';
    topicinput.style.display = 'none';
    booksubmit.style.display = 'none';
    moviesubmit.style.display = 'none';
    groupsubmit.style.display = 'inline-block';
    topicsubmit.style.display = 'none';
};

topicButton.onclick = function () {
    searchtype.innerHTML = '搜索话题(点击其他按钮可更改搜索类别)';
    bookinput.style.display = 'none';
    movieinput.style.display = 'none';
    groupinput.style.display = 'none';
    topicinput.style.display = 'inline-block';
    booksubmit.style.display = 'none';
    moviesubmit.style.display = 'none';
    groupsubmit.style.display = 'none';
    topicsubmit.style.display = 'inline-block';
};
