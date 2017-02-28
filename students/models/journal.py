from django.db import models

from ..models.student import Student


class Journal(models.Model):
    student = models.ForeignKey(Student, max_length=256, verbose_name='Student name', related_name='students',
                                blank=False, unique_for_month='date')
    date = models.DateField(blank=False, verbose_name='Date')
    status = models.BooleanField(default=False, verbose_name='Status')

    class Meta(object):
        verbose_name = 'Journal'
