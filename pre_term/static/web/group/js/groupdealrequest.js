$(function () {
    $('.agree').click(function () {
        let $agree=$(this);
        let applyid=$agree.attr('applyid');
        let is_admin=$agree.attr('is_admin');
        $.getJSON("/web/addgroup/",{"applyid":applyid,"type":"agree"},function (data) {
            console.log(data);
            window.open('/web/groupdealrequest/'+data['groupid'], target="_self");
        })
    });
    $('.disagree').click(function () {
        let $disagree=$(this);
        let is_admin=$disagree.attr('is_admin');
        let applyid=$disagree.attr('applyid');
        $.getJSON("/web/addgroup/",{"applyid":applyid,"type":"disagree"},function (data) {
            console.log(data);
            window.open('/web/groupdealrequest/'+data['groupid'], target="_self");
        })
    })

});