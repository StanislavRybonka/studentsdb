from django.shortcuts import render
from django.views import generic


# Manage Students
class StudentsDataBaseView(generic.TemplateView):
    template_name = 'students/students_list.html'


class StudentsAddView(generic.TemplateView):
    template_name = 'students/student_add_form.html'


class StudentsEditView(generic.TemplateView):
    template_name = "students/students_edit_form.html"


class StudentsDeleteView(generic.TemplateView):
    template_name = 'students/students_delete.html'


# Manage Groups
class GroupsView(generic.TemplateView):
    template_name = "groups/groups.html"


class GroupsAddView(generic.TemplateView):
    template_name = 'groups/groups_add.html'


class GroupsEditView(generic.TemplateView):
    template_name = 'groups/groups_edit.html'


class GroupsDeleteView(generic.TemplateView):
    template_name = 'groups/groups_delete.html'


# Manage Journal
class JournalView(generic.TemplateView):
    template_name = "journal/journal.html"


class JournalSpecificStudentView(generic.TemplateView):
    template_name = 'journal/journal_specific_student.html'


class JournalUpdateView(generic.TemplateView):
    template_name = 'journal/journal_update.html'
