from django.views import generic
from ..models.exam import Exam, ExamResult
from django.shortcuts import render


class ExamsListView(generic.ListView):
    template_name = 'exams/exams_list.html'
    model = Exam
    paginate_by = 10

    def get_queryset(self):
        return Exam.objects.all()


class ExamResultView(generic.ListView):
    template_name = 'exams/exam_results.html'
    model = ExamResult
    paginate_by = 10

    def get_queryset(self):
        return ExamResult.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ExamResultView, self).get_context_data()

        context['student_id'] = self.kwargs.get('student_id')

        return context
