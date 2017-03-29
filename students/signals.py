import logging

from django.db.models.signals import post_save, post_delete
from django.core.signals import request_finished, request_started
from django.dispatch import receiver
from django import dispatch

from django.utils import timezone
from django.core.handlers.wsgi import WSGIHandler
from .models import Student, Group, Exam, LogEntry


@receiver(post_save, sender=Student)
def log_student_updated_added_event(sender, **kwargs):
    '''Writes info abount newly added or updated student into log file'''
    logger = logging.getLogger(__name__)
    student = kwargs['instance']
    if kwargs['created']:
        logger.info('Student added:{} {} (ID:{})'.format(student.first_name, student.last_name, student.id))
    else:
        logger.info('Student updated:{} {} (ID:{})'.format(student.first_name, student.last_name, student.id))


@receiver(post_delete, sender=Student)
def log_student_deleted_event(sender, **kwargs):
    '''Writes info abount deleted student into log file'''

    logger = logging.getLogger(__name__)

    student = kwargs['instance']
    logger.info('Student deleted:{} {} (ID:{})'.format(student.first_name, student.last_name, student.id))


@receiver(post_save, sender=Group)
def log_group_updated_added_event(sender, **kwargs):
    '''Writes info abount newly added or updated group into log file'''
    logger = logging.getLogger(__name__)
    group = kwargs['instance']
    if kwargs['created']:
        logger.info('Group added, title:{} (ID:{})'.format(group.title, group.id))
    else:
        logger.info('Group updated, title:{} (ID:{})'.format(group.title, group.id))


@receiver(post_delete, sender=Group)
def log_group_deleted_event(sender, **kwargs):
    '''Writes info abount deleted group into log file'''

    logger = logging.getLogger(__name__)

    group = kwargs['instance']
    logger.info('Group deleted, title:{} (ID:{})'.format(group.title, group.id))


@receiver(post_save, sender=Exam)
def log_exam_updated_added_event(sender, **kwargs):
    '''Writes info abount newly added or updated Exam into log file'''
    logger = logging.getLogger(__name__)
    exam = kwargs['instance']

    if kwargs['created']:
        logger.info('Exam was added, discipline:{} (ID:{})'.format(exam.discipline_name, exam.id))
    else:
        logger.info('Exam was updated, discipline:{} (ID:{})'.format(exam.discipline_name, exam.id))


@receiver(post_delete, sender=Exam)
def log_exam_deleted_event(sender, **kwargs):
    '''Writes info abount deleted Exam into log file'''

    logger = logging.getLogger(__name__)

    exam = kwargs['instance']
    logger.info('Exam was deleted, discipline:{} (ID:{})'.format(exam.discipline_name, exam.id))


contact_admin_signal = dispatch.Signal(providing_args=["from_email"])


@receiver(contact_admin_signal)
def contact_admin_signal_handler(sender, **kwargs):
    email = kwargs.get('from_email')

    logger = logging.getLogger(__name__)

    logger.info('Email successful sended to administration, user email: {}'.format(email))


from django.db.models import F

@receiver(request_started, sender=WSGIHandler)
def count_request_handler(sender, **kwargs):
    if request_finished:
        LogEntry.objects.filter(date__lte=timezone.now()).update(request_counter=F('request_counter') + 1)

