from ..forms import ContactForm
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from ..models.log_entry import LogEntry

import logging
from students.signals import contact_admin_signal


class ContactUsView(SuccessMessageMixin, generic.FormView):
    template_name = 'contact_us/contact_us_form.html'
    form_class = ContactForm
    success_url = '/contact-admin'
    success_message = 'Message send successful'

    def form_valid(self, form):
        form.send_email()

        contact_admin_signal.send(sender=self.__class__, from_email=self.request.POST['from_email'])

        return super(ContactUsView, self).form_valid(form)

    def form_invalid(self, form):
        message = 'During sending process occurs issues.Try again later.'

        logger = logging.getLogger(__name__)

        logger.exception(message)

        return super(ContactUsView, self).form_invalid(form)
