$(function () {
    $('.is_delete').click(function () {
        let $is_delete=$(this);
        let comment_id = $is_delete.attr('comment_id');
        $.getJSON("/web/t_comment/",{"comment_id" : comment_id,"type" : "delete"},function (data) {
            console.log(data);
            window.location.reload();
        })
    })
});