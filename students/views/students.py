from django.shortcuts import render
from django.views import generic
from ..models import Student


# Manage Students
class StudentsListView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        students = Student.objects.order_by('last_name').all()

        #Try to order students list
        order_by = request.GET.get('order_by', '')
        if order_by in ('last_name', 'first_name', 'ticket'):
            students = students.order_by(order_by)
            if request.GET.get('reverse', '') == '1':
                students = students.reverse()
        return render(request, 'students/students_list.html', {'students': students})


class StudentsAddView(generic.TemplateView):
    template_name = 'students/student_add_form.html'


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
