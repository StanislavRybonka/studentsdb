from django.shortcuts import render
from django.views import generic


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
