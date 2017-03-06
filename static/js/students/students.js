/**
 * Created by sr on 06.03.17.
 */

function initStudentPage() {
    // Обробити клік по кнопці Студенти, отримати url адресу

    $('.nav-tabs li a').click(function (event) {
        var url_address = $(this);
        $('.nav-tabs li').removeClass('active');
        $(this).parent().addClass('active');

        $.ajax({
            'url': url_address.attr('href'),
            'dataType': 'html',
            'type': 'get',
            'success': function (data, status, xhr) {

            var html = $(data);
            var body = html.find('#content-column');
            $('#content-columns').html(body);

            }

        });


        return false
    });

    // Додати клас (активний едемент) до меню

    //Отримати html із даними зі сторінки
}


$(document).ready(function () {
    initStudentPage();
});