from django.conf.urls import include, url

from .views import StudentsDataBaseView, StudentsGroupView, CountVisitsView, StudentsEditView

urlpatterns = [
    url(r'^students/$', StudentsDataBaseView.as_view(), name="students_db"),
    url(r'^group/$', StudentsGroupView.as_view(), name="students_group"),
    url(r'^visits/$', CountVisitsView.as_view(), name="count_visits"),
    url(r'^edit/$', StudentsEditView.as_view(), name="edit_students")

]
