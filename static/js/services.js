
$(document).ready(function() {

    $('#load_more').click(function () {

        $.ajax({
            type: "GET",
            url: "/",
            success: function (data) {
                console.log('Hello from ajax view');
                var object_list = JSON.parse(data.data);
                for(var i = 0;i< object_list.length;i++){
                    console.log(object_list[i].fields.first_name);
                     $('.test').append('<tr><td>'+object_list[i].fields.first_name+'</td></tr>')
                }








            }
        });

    });
});