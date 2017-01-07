from django.shortcuts import render
from django.views import generic


# Manage Students
class StudentsListView(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        students = {
                       'id': 1,
                       'first_name': 'Stanislav',
                       'last_name': 'Rybonka',
                       'ticket': 255,
                       'image': 'img/foto1.jpg'
                   },
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
