$(function () {
    let $topic_name=$('#topic_name');
    $topic_name.change(function () {
        let topic_name = $topic_name.val().trim();
        if(topic_name.length){
            $.getJSON('/web/checktopic/', {'topic_name':topic_name}, function (data) {
                console.log(data);
                let $username_info = $("#topiccreatewrong");
                if (data['status'] === 200) {
                    $username_info.html("话题名称可用").css("color", 'green');
                } else if (data['status'] === 900) {
                    $username_info.html("话题名称已存在").css("color", 'red');
                }
            })
        }
    })
});

function check() {

    let $topic_name=$('#topic_name');
    let $topic_type=$('#topic_type');
    let topic_name = $topic_name.val().trim();
    let topic_type = $topic_type.val().trim();
    if (!topic_name) {
        return false;
    }
    if (topic_type !== '书籍' && topic_type !== '影视' && topic_type !== '其他') {
        return false;
    }
    let info_color = $("#topiccreatewrong").css('color');

    console.log(info_color);

    return info_color !== 'rgb(255, 0, 0)';


}