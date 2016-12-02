from django.shortcuts import render
from django.views import generic


class StudentsDataBaseView(generic.TemplateView):
    template_name = 'students_database.html'


class StudentsGroupView(generic.TemplateView):
    template_name = "students_group.html"


class CountVisitsView(generic.TemplateView):
    template_name = "count_visits.html"


class StudentsEditView(generic.TemplateView):
    template_name = "students_edit_form.html"
