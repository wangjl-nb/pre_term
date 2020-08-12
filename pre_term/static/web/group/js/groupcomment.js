$(function () {
    $('.is_essential').click(function () {
        let $is_essential=$(this);
        let comment_id = $is_essential.attr('comment_id');
        $.getJSON("/web/g_comment/",{"comment_id" : comment_id,"type" : "essential"},function (data) {
            console.log(data);
            window.location.reload();
        })
    });
    $('.is_top').click(function () {
        let $is_top=$(this);
        let comment_id = $is_top.attr('comment_id');
        $.getJSON("/web/g_comment/",{"comment_id" : comment_id,"type" : "top"},function (data) {
            console.log(data);
            window.location.reload();
        })
    });
    $('.is_delete').click(function () {
        let $is_delete=$(this);
        let comment_id = $is_delete.attr('comment_id');
        $.getJSON("/web/g_comment/",{"comment_id" : comment_id,"type" : "delete"},function (data) {
            console.log(data);
            window.location.reload();
        })
    })
});