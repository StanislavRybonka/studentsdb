from __future__ import unicode_literals

from django.db import models


class Group(models.Model):
    '''Group model'''

    title = models.CharField(max_length=256, blank=False, verbose_name='Name')
    leader = models.OneToOneField('Student', verbose_name='Leader', blank=True, null=True, on_delete=models.SET_NULL)
    notes = models.TextField(blank=True, verbose_name='Additional notices')

    class Meta(object):
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    def __str__(self):
        if self.leader:
            return '{}({}{})'.format(self.title, self.leader.first_name, self.leader.last_name)
        else:
            return '{}'.format(self.title)
