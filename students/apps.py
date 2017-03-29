from __future__ import unicode_literals

from django.apps import AppConfig

from django.db.models.signals import post_migrate
import logging


def log_migrate(sender, **kwargs):
    log = kwargs['plan']

    if log:

        logger = logging.getLogger(__name__)

        logger.info('Migration apllied: {}'.format(log))


class StudentsAppConfig(AppConfig):
    name = 'students'
    verbose_name = 'Students DB'

    def ready(self):
        from students import signals
        post_migrate.connect(log_migrate, sender=self)
