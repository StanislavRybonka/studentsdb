function initJournal() {
    var indicator = $('#ajax-progress-indicator');
    var show_errors = $('#ajax-request-errors');

    $('.day-box input[type="checkbox"]').click(function (event) {
        var box = $(this);
        $.ajax(box.data('url'), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'pk': box.data('student-id'),
                'date': box.data('date'),
                'present': box.is(':checked') ? '1' : '',
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            'beforeSend': function (xhr, settings) {
                indicator.show();
            },
            'error': function (xhr, status, error) {
                indicator.hide();
                show_errors.show();
                show_errors.html(error);
                setTimeout(function () {

                    show_errors.hide();


                }, 2000);

            },
            'success': function (data, status, xhr) {
                indicator.hide();

            }
        })

    })

}


function initGroupSelector() {
    // look up select elemnt with groups and attach our even handler
    // on find change event
    $('#group-selector select').change(function (event) {
        var group = $(this).val();

        if (group) {
            // set cookie with expiration date q year since now
            // cookie creation function takes period in days
            $.cookie('current_group', group, {'path': '/', 'expires': 365});
        } else {
            // otherwise we delete the cookie
            $.removeCookie('current_group', {'path': '/'});
        }

        // and reload a page
        location.reload(true);

        return true;

    })
}


function initDateFields() {
    $('input.dateinput').datetimepicker({
        'format': 'YYYY-MM-DD'

    }).on('dp.hide', function (event) {
        $(this).blur();

    });

}


function initEditStudentPage() {
  $('a.student-edit-form-link').click(function(event){
    var link = $(this);
    $.ajax({
      'url': link.attr('href'),
      'dataType': 'html',
      'type': 'get',
      'success': function(data, status, xhr){
        // check if we got successfull response from the server
        if (status != 'success') {
          alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
          return false;
        }

        // update modal window with arrived content from the server
        var modal = $('#myModal'),
          html = $(data), form = html.find('#content-column form');
        modal.find('.modal-title').html(html.find('#content-column h2').text());
        modal.find('.modal-body').html(form);

        // init our edit form


        // setup and show modal window finally
        modal.modal({
          'show': true
        });
      },
      'error': function(){
          alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
          return false
      }
    });

    return false;
  });
}

$(document).ready(function () {
    initJournal();
    initGroupSelector();
    initDateFields();
    initEditStudentPage();
});