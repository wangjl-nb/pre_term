$(function () {
    let $group_id=$('#group_id');
    $group_id.change(function () {
        let group_id = $group_id.val().trim();
        if(group_id.length){
            $.getJSON('/web/checkgroup/', {'group_id':group_id}, function (data) {
                console.log(data);
                let $username_info = $("#groupcreatewrong");
                if (data['status'] === 200) {
                    $username_info.html("小组账号可用").css("color", 'green');
                } else if (data['status'] === 900) {
                    $username_info.html("小组账号已存在").css("color", 'red');
                }
            })
        }
    })
});

function check() {

    let $group_id=$('#group_id');
    let group_id = $group_id.val().trim();
    let $group_name=$('#group_name');
    let group_name = $group_name.val().trim();
    if (!group_id||!group_name) {
        return false;
    }

    let info_color = $("#groupcreatewrong").css('color');

    console.log(info_color);

    return info_color !== 'rgb(255, 0, 0)';


}