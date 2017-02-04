from django.conf.urls import url

from students.views import students as students_views, groups as groups_views, journal as journal_views,exams as exams_views

urlpatterns = [
    # Students urls
    url(r'^$', students_views.StudentsListView.as_view(), name='students_list'),
    url(r'^students/add/$', students_views.student_add, name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', students_views.StudentsEditView.as_view(), name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', students_views.StudentsDeleteView.as_view(), name='students_delete'),

    # Groups urls
    url(r'^groups/$', groups_views.GroupsListView.as_view(), name="groups_list"),
    url(r'^groups/add/$', groups_views.GroupsAddView.as_view(), name='groups_add'),
    url(r'^groups/(?P<gid>\d+)/edit/$', groups_views.GroupsEditView.as_view(), name='groups_edit'),
    url(r'^groups/(?P<gid>\d+)/delete/$', groups_views.GroupsDeleteView.as_view(), name='groups_delete'),

    # Journal urls
    url(r'^journal/$', journal_views.JournalView.as_view(), name="journal"),
    url(r'^journal/(?P<jid>\d+)/$', journal_views.JournalSpecificStudentView.as_view(),
        name="journal_specific_student"),
    url(r'^journal/update/$', journal_views.JournalUpdateView.as_view(), name="journal_update"),

    # Exams List url
    url(r'^exams/$', exams_views.ExamsListView.as_view(), name='exams_list'),
    url(r'^exams-result/(?P<student_id>\d+)/$', exams_views.ExamResultView.as_view(), name='exams_results')

]
