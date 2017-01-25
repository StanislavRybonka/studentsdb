
$(document).ready(function() {

    $('#load_more').click(function () {

        $.ajax({
            type: "GET",
            url: "/",
            success: function (data) {
                console.log('Hello from ajax view');
                var object_list = JSON.parse(data.data);

                console.log(typeof (object_list));



                $('.test').append(data.data)

            }
        });

    });
});