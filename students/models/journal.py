from django.db import models

from ..models.student import Student


class Journal(models.Model):
    student = models.ForeignKey(Student, max_length=256, verbose_name='Student name', related_name='students',
                                blank=False, unique_for_month='date')
    date = models.DateField(blank=False, verbose_name='Date')
    status = models.BooleanField(default=False, verbose_name='Status')

for i in range(1,31):
    Journal.add_to_class('present_day_%s' % i, models.BooleanField(default=False))

    class Meta(object):
        verbose_name = 'Journal'
