var urls = {};
urls.ajax_prefix = '/ajax/';
urls.get_sidebar = urls.ajax_prefix + 'get_sidebar';

var sidebar = $('#sidebar');

function get_sidebar() {
    request = $.ajax({url: urls.get_sidebar});
    request.done(function(msg) {
        sidebar.html(msg);
    });
}

$(document).ready(function() {
    get_sidebar();
});
