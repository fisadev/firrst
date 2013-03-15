var urls = {};
urls.ajax_prefix = '/ajax/';
urls.get_sidebar = urls.ajax_prefix + 'get_sidebar';
urls.get_feed = urls.ajax_prefix + 'get_feed/%feed_id%/';

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
    request = $.ajax({url: urls.get_feed.replace('%feed_id%', feed_id)});
    request.done(function(msg) {
        gui.content.html(msg);
    });
}

$(document).ready(function() {
    gui.sidebar = $('#sidebar');
    gui.content = $('#content');

    get_sidebar();
});
