from django.db import models


class LogEntry(models.Model):
    error_level = models.CharField(max_length=20, verbose_name='Level')
    date = models.DateTimeField()
    error_message = models.CharField(max_length=1000, verbose_name='Message')



