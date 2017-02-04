from django.shortcuts import render
from django.views import generic
from ..models.student import Student
from ..models.group import Group
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import datetime


# Manage Students
class StudentsListView(generic.ListView):
    model = Student
    paginate_by = 5
    template_name = 'students/students_list.html'

    def get_queryset(self):
        queryset = Student.objects.order_by('last_name').all()

        order_by = self.request.GET.get('order_by', '')
        if order_by in ('last_name', 'first_name', 'ticket'):
            students = queryset.order_by(order_by)
            if self.request.GET.get('reverse', '') == '1':
                queryset = students.reverse()

        return queryset


def student_add(request):
    # If form is submited:
    if request.method == 'POST':
        if request.POST.get('add_button') is not None:
            # To do validate
            errors = {}

            # prepare dict here for  future data - info
            data = {'middle_name': request.POST.get('middle_name'), 'notes': request.POST.get('notes')}

            # validate user inputs
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = 'Name is demand'
            else:
                data['first_name'] = first_name

            #delete free space with strip()
            last_name = request.POST.get('last_name', '').strip()
            if not last_name:
                errors['last_name'] = "Last name is demand"
            else:
                data['last_name'] = last_name

            birthday = request.POST.get('birthday', '').strip()
            if not birthday:
                errors['birthday'] = 'Birthday field is demand'
            else:
                try:
                    # set format for date
                    datetime.strptime(birthday, '%Y-%m-%d')

                except Exception:

                    errors['birthday'] = 'Enter right format'
                else:
                    data['birthday'] = birthday

            ticket = request.POST.get('ticket', '').strip()

            if not ticket:
                errors['ticket'] = 'Ticket field is demand'
            else:
                data['ticket'] = ticket

            student_group = request.POST.get('student_group', '').strip()
            if not student_group:
                errors['student_group'] = 'Group is demand'
            else:
                # For Model with Foreight key we use second tricks
                groups = Group.objects.filter(pk=student_group)
                if len(groups) != 1:
                    errors['student_group'] = 'Choose right group'
                else:
                    data['student_group'] = groups[0]

            photo = request.FILES.get('photo')
            if photo:
                data['photo'] = photo

            if not errors:
                # after all we take dat and save it
                student = Student(**data)
                # save it to db
                student.save()

                # redirect user to students_list, pay atention on status message, send it via GET
                return HttpResponseRedirect('%s?status_message=Successful added'% reverse('students_list'))
            else:
                # render form with errors and previous user's input
                return render(request, 'students/student_add_form.html',
                              {'groups': Group.objects.all().order_by('title'), 'errors': errors})

        elif request.POST.get('cancel_button') is not None:
            # redirect to students list on cancel button
            return HttpResponseRedirect('%s?status_message=Canceled'% reverse('students_list'))
    else:
        # initial form render
        return render(request, 'students/student_add_form.html', {'groups': Group.objects.all().order_by('title')})


class StudentsEditView(generic.TemplateView):
    template_name = "students/students_edit_form.html"

    def get_context_data(self, **kwargs):
        context = super(StudentsEditView, self).get_context_data(**kwargs)

        context['sid'] = self.kwargs.get('sid')
        return context


class StudentsDeleteView(generic.TemplateView):
    template_name = 'students/students_delete.html'

    def students_delete(self, request, sid):
        return render(self.request, sid)
