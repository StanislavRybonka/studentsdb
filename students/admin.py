from django.contrib import admin
from .models import Student, Group, Journal, Exam
from .models.exam import ExamResult
from django.core.urlresolvers import reverse
from django.forms import ModelForm, ValidationError


class StudentFormAdmin(ModelForm):
    def clean_student_group(self):
        """Check if student is leader in any group
        If yes, then ensure it's the same as selected group"""
        # get group where current student is leader
        groups = Group.objects.filter(leader=self.instance)
        if len(groups) > 0 and self.cleaned_data['student_group'] != [0]:
            raise ValidationError('Student are leader in other group', code='invalid')

        return self.cleaned_data['student_group']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'ticket', 'student_group']
    list_display_links = ['last_name', 'first_name']
    list_editable = ['student_group']
    list_filter = ['student_group']
    list_per_page = 10
    search_fields = ['last_name', 'first_name', 'middle_name', 'ticket', 'notes']
    form = StudentFormAdmin

    def get_view_on_site_url(self, obj=None):
        return reverse('students_edit', kwargs={'pk': obj.id})


# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Group)
admin.site.register(Journal)
admin.site.register(Exam)
admin.site.register(ExamResult)
