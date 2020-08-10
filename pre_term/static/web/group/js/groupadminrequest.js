function windowOn(window, button) {
    button.addEventListener('click', function () {
        window.style.display = 'block';
        maskbg.style.display = 'block';
    })
}
function close(window, close) {
    close.addEventListener('click', function () {
        window.style.display = 'none';
        maskbg.style.display = 'none';
    })
}
var maskbg = document.getElementById('maskbg');
var groupAdminRequest = document.getElementById('groupAdminRequest');
var groupAdminRequestLink = document.getElementById('groupAdminRequestLink');
var groupAdminRequestClose = document.getElementById('groupAdminRequestClose');
windowOn(groupAdminRequest, groupAdminRequestLink);
close(groupAdminRequest, groupAdminRequestClose);
