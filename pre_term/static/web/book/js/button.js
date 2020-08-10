$(function () {
    $('.likeButton').click(function () {
        let $like=$(this);
        let comment_id = $like.attr('comment_id');
        console.log(comment_id);
        $.getJSON("/web/dealcomment/",{"commentid":comment_id,"type":"like"},function (data) {
            console.log(data);
            if(data['status']===302){
                window.open('/web/login/',target="_self");
            }
            else
                window.location.reload();
        })
    });
    $('.dislikeButton').click(function () {
        let $dislike=$(this);
        let comment_id = $dislike.attr('comment_id');
        $.getJSON("/web/dealcomment/",{"commentid":comment_id,"type":"dislike"},function (data) {
            console.log(data);
            if(data['status']===302){
                window.open('/web/login/',target="_self");
            }
            else
                window.location.reload();
        })
    });
    $('.deleteButton').click(function () {
        let $delete=$(this);
        let comment_id = $delete.attr('comment_id');
        $.getJSON("/web/deletecomment/",{"commentid":comment_id},function (data) {
            console.log(data);
            if(data['status']===302){
                window.open('/web/login/',target="_self");
            }
            else
                window.location.reload();
        })
    })
});