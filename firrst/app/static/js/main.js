var urls = {};
urls.ajax_prefix = '/ajax/';
urls.get_sidebar = urls.ajax_prefix + 'get_sidebar';

var gui = {};

function get_sidebar() {
    request = $.ajax({url: urls.get_sidebar});
    request.done(function(msg) {
        gui.sidebar.html(msg);
        gui.sidebar.find('li').on('click', function(e){
            e.preventDefault();
            show_feed($(this).attr('data-feedid'));
        });
    });
}

function show_feed(feed_id) {
    alert(feed_id);
}

$(document).ready(function() {
    gui.sidebar = $('#sidebar');

    get_sidebar();
});
