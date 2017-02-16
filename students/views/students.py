from django.views import generic
from ..models.student import Student
from django.core.urlresolvers import reverse, reverse_lazy
from ..forms import StudentForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Manage Students
def students_list(request):
    template_name = 'students/students_list.html'

    # take students list queryset
    students = Student.objects.all()

    # check request method is GET
    if request.method == 'GET':
        order_by_data = request.GET.get('order_by')
        order_by_reverse = request.GET.get('reverse')

        # if method is GET, need receive arguments for order by
        if order_by_data:
            students = students.order_by(order_by_data)

        if order_by_reverse:
            students = students.order_by(order_by_data).reverse()

    # add simple pagination
    paginator = Paginator(students, 10)

    page = request.GET.get('page')

    try:
        students = paginator.page(page)

    except PageNotAnInteger:
        students = paginator.page(1)

    except EmptyPage:
        students = paginator.page(paginator.num_pages)

    # return value according to order_by data

    return render(request, template_name, {'object_list': students})


class StudentAddView(SuccessMessageMixin, generic.CreateView):
    template_name = 'students/student_add_form.html'
    form_class = StudentForm
    model = Student
    success_url = reverse_lazy('students_list')
    success_message = '%(first_name)s %(last_name)s Successfull added to datebase!'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # To do notify student by email that he is added to group
        return super(StudentAddView, self).form_valid(form)


class StudentsEditView(SuccessMessageMixin, generic.UpdateView):
    template_name = "students/students_edit_form.html"
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('students_list')
    success_message = '%(first_name)s %(last_name)s Successfull updated!'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        # To do notify student by email that he is added to group
        return super(StudentsEditView, self).form_valid(form)


class StudentsDeleteView(generic.DeleteView):
    model = Student
    template_name = 'students/students_confirm_delete.html'

    def get_success_url(self):
        return reverse('students_list',
                       messages.add_message(self.request, messages.SUCCESS, 'Student successful deleted'))
