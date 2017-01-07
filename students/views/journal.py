from django.shortcuts import render
from django.views import generic


# Manage Journal
class JournalView(generic.TemplateView):
    template_name = "journal/journal.html"


class JournalSpecificStudentView(generic.TemplateView):
    template_name = 'journal/journal_specific_student.html'

    def get_student(self, request, jid):
        return render(self, request, jid)


class JournalUpdateView(generic.TemplateView):
    template_name = 'journal/journal_update.html'
