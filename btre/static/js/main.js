const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// fade out alert message ie in account registeration form
// python manage.py collectstatic after to:- btre\static to main static
setTimeout(function() {
    $('#message').fadeOut('slow');
}, 3000);