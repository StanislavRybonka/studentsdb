from __future__ import unicode_literals

from django.db import models


class Student(models.Model):
    '''Student model'''

    first_name = models.CharField(max_length=256, blank=False, verbose_name='Name')
    last_name = models.CharField(max_length=256, blank=False, verbose_name='Surname')
    middle_name = models.CharField(max_length=256, blank=True, verbose_name='Second name', default='')
    birthday = models.DateField(blank=False, verbose_name='Date of birthday', null=True)
    photo = models.ImageField(blank=True, verbose_name='Foto', null=True)
    ticket = models.CharField(max_length=256, blank=False, verbose_name='Ticket')
    notes = models.TextField(blank=True, verbose_name='Additional notices')

    class Meta(object):
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['last_name']

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)
