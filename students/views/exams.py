from django.views import generic
from ..models.exam import ExamResult
from ..models.exam import Exam
from ..forms import ExamForm
from  django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import reverse
from django.contrib import messages


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


class ExamAddView(SuccessMessageMixin, generic.CreateView):
    model = Exam
    template_name = 'exams/exam_add_form.html'
    form_class = ExamForm
    success_url = '/exams'
    success_message = 'New exam of %(discipline_name)s had been addded to DB!'


class ExamEditView(SuccessMessageMixin, generic.UpdateView):
    model = Exam
    template_name = 'exams/exam_edit_form.html'
    form_class = ExamForm
    success_url = '/exams'
    success_message = '%(discipline_name)s was updated!'


class ExamDeleteView(generic.DeleteView):
    model = Exam
    template_name = 'exams/exam_delete_confirm.html'

    def get_success_url(self):
        return reverse('exams_list', messages.add_message(self.request, messages.SUCCESS, 'Exam deleted successful!'))