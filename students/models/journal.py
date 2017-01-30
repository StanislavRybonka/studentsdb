from django.db import models
from django import forms


class Journal(models.Model):
    name = models.ForeignKey('Student', max_length=256, verbose_name='Student name', blank=False)
    status = models.BooleanField(default=False, verbose_name='Status')
    date = models.DateField(blank=True, verbose_name='Date')

    class Meta(object):
        verbose_name = 'Journal'
