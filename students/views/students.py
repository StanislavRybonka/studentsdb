from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from ..models import Student
from django.http import JsonResponse


# Manage Students
class StudentsListView(generic.View):
    model = Student
    # paginate_by = 20
    template_name = 'students/students_list.html'

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            var = 10
            return JsonResponse({
                'data':var
            })
        return render(request, self.template_name, { 'white_ip_list': 2})

    # def get_queryset(self):
    #     students = Student.objects.order_by('last_name').all()
    #
    #     order_by = self.request.GET.get('order_by', '')
    #     if order_by in ('last_name', 'first_name', 'ticket'):
    #         students = students.order_by(order_by)
    #         if self.request.GET.get('reverse', '') == '1':
    #             students = students.reverse()
    #     return students


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
