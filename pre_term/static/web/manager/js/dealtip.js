$(function () {
    $('.agree').click(function () {
        let $agree=$(this);
        let tip_type=$agree.attr('tip_type');
        let tip_id=$agree.attr('tip_id');
        let comment_id=$agree.attr('comment_id');
        $.getJSON("/web/dealtipfunction/",{"tip_id":tip_id,"type":"agree","tip_type":tip_type,"comment_id":comment_id},function (data) {
            console.log(data);
            window.open('/web/dealtip/', target="_self");
        })
    });
    $('.disagree').click(function () {
        let $disagree=$(this);
        let tip_type=$disagree.attr('tip_type');
        let tip_id=$disagree.attr('tip_id');
        let comment_id=$disagree.attr('comment_id');
        $.getJSON("/web/dealtipfunction/",{"tip_id":tip_id,"type":"disagree","tip_type":tip_type,"comment_id":comment_id},function (data) {
            console.log(data);
            window.open('/web/dealtip/', target="_self");
        })
    })

});