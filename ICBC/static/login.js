// console.log('hi')

$(function () {
    $('#submit').click(function (event) {
        event.preventDefault();
        event.preventDefault();
        var email = $('input[name=email]').val();
        var password = $('input[name=password]').val();
        // var csrftoken = $('input[name=csrf_token]').val();

        icbcajax.post({
            'url': '/login/',
            'data':{
                'email': email,
                'password': password,
                // 'csrf_token': csrftoken
            },
            'success':function (data) {
                console.log(data);
            },
            'fail': function (error) {
                console.log(error);
            }
        });
    });
});