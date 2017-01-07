from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse


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


# Manage Groups
class GroupsListView(generic.TemplateView):
    template_name = "groups/groups.html"


class GroupsAddView(generic.TemplateView):
    template_name = 'groups/groups_add.html'


class GroupsEditView(generic.TemplateView):
    template_name = 'groups/groups_edit.html'

    def groups_edit(self, request, gid):
        return render(self.request, gid)


class GroupsDeleteView(generic.TemplateView):
    template_name = 'groups/groups_delete.html'

    def groups_delete(self, request, gid):
        return render(self.request, gid)


# Manage Journal
class JournalView(generic.TemplateView):
    template_name = "journal/journal.html"


class JournalSpecificStudentView(generic.TemplateView):
    template_name = 'journal/journal_specific_student.html'

    def get_student(self, request, jid):
        return render(self, request, jid)


class JournalUpdateView(generic.TemplateView):
    template_name = 'journal/journal_update.html'
