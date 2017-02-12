from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.core.urlresolvers import reverse
from students.models import Student
import magic
from django.core.exceptions import ValidationError
from studentsdb.settings import CONTENT_TYPES, MAX_UPLOAD_SIZE
from django.core.mail import send_mail
from studentsdb.local_settings import MANAGERS

from .models.group import Group

from .models.exam import Exam


# Students FORM

class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Your Email')
    subject = forms.CharField(label='Subject', max_length=128)
    message = forms.CharField(label='Message text', max_length=2500, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        # call origin initializator
        super(ContactForm, self).__init__(*args, **kwargs)

        # this helper object allow us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact-admin')

        # twiter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control-label'
        self.helper.field_class = 'col-sm-10'

        # form button
        self.helper.add_input(Submit('send_button', 'Send'))

    def send_email(self):
        email_from = self.cleaned_data.get('from_email')
        subject = self.cleaned_data.get('subject')
        message = self.cleaned_data.get('message')

        return send_mail(subject, message, email_from, MANAGERS)


class StudentForm(forms.ModelForm):
    last_name = forms.CharField(validators=[])

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'photo', 'ticket', 'notes', 'student_group']

    def clean_photo(self):
        cleaned_data = super(StudentForm, self).clean()
        file = cleaned_data.get('photo')

        if file:
            file_type = magic.from_buffer(file.read(), mime=True).format().split('/')[1].upper()

            if not file_type in CONTENT_TYPES:

                self.add_error('photo', forms.ValidationError('Invalid format for images, recommended PNG'))


            elif file.size > MAX_UPLOAD_SIZE:

                raise ValidationError('Invalid size.')

    def clean_first_name(self):
        name = self.cleaned_data.get('first_name')
        if len(name) < 3:
            self.add_error('first_name', ValidationError('Short name'))
        else:
            return name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if last_name[0].isupper():
            return last_name
        else:
            self.add_error('last_name', ValidationError('First litter should be Capitalize'))


# Group FORM

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'leader', 'notes']

        # To do, add some validation here if need


# Exam Form

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['discipline_name', 'date', 'teacher_name', 'group_id']
