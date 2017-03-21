from __future__ import unicode_literals

from django.apps import AppConfig


class StudentsAppConfig(AppConfig):
    name = 'students'
    verbose_name = 'Students DB'

    def ready(self):
        from students import signals
