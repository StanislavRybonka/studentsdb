from django.conf.urls import include, url

from cabinet import views

urlpatterns = [
    # Students urls
    url(r'^students/$', views.StudentsDataBaseView.as_view(), name='students_list'),
    url(r'^students/add/$', views.StudentsAddView.as_view(), name='add_new_student'),
    url(r'^edit/$', views.StudentsEditView.as_view(), name='edit_student'),
    url(r'^students/delete/$', views.StudentsDeleteView.as_view(), name='delete_student'),

    # Groups urls
    url(r'^groups/$', views.GroupsView.as_view(), name="groups"),
    url(r'^groups/add/$', views.GroupsAddView.as_view(), name='add_groups'),
    url(r'^groups/123/edit/$', views.GroupsEditView.as_view(), name='edit_groups'),
    url(r'^groups/123/delete/$', views.GroupsDeleteView.as_view(), name='delete_groups'),

    # Journal urls
    url(r'^journal/$', views.JournalView.as_view(), name="journal"),
    url(r'^journal/123$', views.JournalSpecificStudentView.as_view(), name="journal_specific_student"),
    url(r'^journal/update/$', views.JournalUpdateView.as_view(), name="journal_update"),

]
