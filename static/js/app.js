$(document).ready(function() {
    var socket = io.connect("http://172.16.156.139:5000")

    socket.on('connect', function() {
        socket.send("User connected!");
    });

    socket.on('message', function(data) {
        $('#messages').append($('<p>').text("> " + data));
        setTimeout(makeMsgVisible, 1);
    });

    $('#sendBtn').on('click', function() {
        sendMsg(socket)
    });

    $('body').on('keydown', function(e) {
        if(e.key == "Enter") {
            sendMsg(socket);
        }
    });

    $('.switch label').on('click', toggleDark);
});

function sendMsg(socket) {
    socket.send($("#message").val());
    $('#message').val('');
}

function toggleDark() {
    $('body').toggleClass('dark');
}

function makeMsgVisible() {
    document.querySelectorAll('p').forEach(function(elem) {
        if(!elem.classList.contains('visible')) {
            elem.classList.add('visible');
        }
    })
}
