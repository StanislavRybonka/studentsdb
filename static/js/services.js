
$(document).ready(function() {

    $('#load_more').click(function () {

        $.ajax({
            type: "GET",
            url: "/",
            success: function (data) {
                console.log('Hello from ajax view');
                $('.test').append(data.data)

            }
        });

    });
});