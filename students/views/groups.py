from django.shortcuts import render
from django.views import generic
from ..models.group import Group


# Manage Groups
class GroupsListView(generic.ListView):
    template_name = "groups/groups.html"
    model = Group
    paginate_by = 10

    def get_queryset(self):
        queryset = Group.objects.all()
        order_by = self.request.GET.get('order_by', '')
        if order_by in ('title', 'leader',):
            queryset = queryset.order_by(order_by)
            if self.request.GET.get('reverse', '') == '1':
                queryset = queryset.reverse()

        return queryset


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
