from django.conf.urls import include, url

from cabinet import views

urlpatterns = [
    # Students urls
    url(r'^$', views.StudentsListView.as_view(), name='students_list'),
    url(r'^students/add/$', views.StudentsAddView.as_view(), name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', views.StudentsEditView.as_view(), name='students_edit'),
    url(r'^students/(?P<sid>\d+)delete/$', views.StudentsDeleteView.as_view(), name='students_delete'),

    # Groups urls
    url(r'^groups/$', views.GroupsListView.as_view(), name="groups_list"),
    url(r'^groups/add/$', views.GroupsAddView.as_view(), name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', views.GroupsEditView.as_view(), name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', views.GroupsDeleteView.as_view(), name='groups_delete'),

    # Journal urls
    url(r'^journal/$', views.JournalView.as_view(), name="journal"),
    url(r'^journal/(?P<jid>\d+)/$', views.JournalSpecificStudentView.as_view(), name="journal_specific_student"),
    url(r'^journal/update/$', views.JournalUpdateView.as_view(), name="journal_update"),

]
