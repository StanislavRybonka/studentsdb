from django.shortcuts import render
from  django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from ..forms import ContactForm
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin

from studentsdb.local_settings import ADMIN_EMAIL


class ContactUsView(SuccessMessageMixin, generic.FormView):
    template_name = 'contact_us/contact_us_form.html'
    form_class = ContactForm
    success_url = '/contact-admin'
    success_message = 'Message send successful'

    def form_valid(self, form):
        form.send_email()
        return super(ContactUsView, self).form_valid(form)
