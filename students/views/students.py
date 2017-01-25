from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
from ..models import Student
from django.http import JsonResponse
from django.views.generic.list import MultipleObjectMixin
from django.conf import settings
from django.shortcuts import render_to_response
import json
from django.core import serializers


# Manage Students
class StudentsListView(generic.ListView):
    model = Student
    paginate_by = 20
    template_name = 'students/students_list.html'

    def get(self, request, **kwargs):
        students = Student.objects.order_by('last_name').all()

        order_by = self.request.GET.get('order_by', '')
        if order_by in ('last_name', 'first_name', 'ticket'):
            students = students.order_by(order_by)
            if self.request.GET.get('reverse', '') == '1':
                students = students.reverse()
        if request.is_ajax():
            self.object_list = self.get_queryset()
            context = super(StudentsListView, self).get_context_data(**kwargs)
            data = serializers.serialize("json", students)
            return JsonResponse({
                'data':data
            })
        return super(StudentsListView, self).get(request, **kwargs)


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
