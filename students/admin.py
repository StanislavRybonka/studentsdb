from django.contrib import admin
from .models import Student,Group,Journal,Exam
from .models.exam import ExamResult

# Register your models here.
admin.site.register(Student)
admin.site.register(Group)
admin.site.register(Journal)
admin.site.register(Exam)
admin.site.register(ExamResult)
