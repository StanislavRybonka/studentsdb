from django.db import models


class Exam(models.Model):
    discipline_name = models.CharField(max_length=256, verbose_name='Discipline name', blank=False)
    date = models.DateTimeField(verbose_name='Date', blank=False)
    teacher_name = models.CharField(max_length=256, verbose_name='Teacher name', blank=False)
    group_id = models.ForeignKey('Group', verbose_name='Group', blank=True, null=True)

    class Meta(object):
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'

    def __unicode__(self):
        return '{}'.format(self.discipline_name)


class ExamResult(models.Model):
    exam_id = models.ForeignKey('Exam', verbose_name='Exam', blank=True)
    student_id = models.ForeignKey('Student', verbose_name='Student', blank=True)
    rating = models.FloatField(verbose_name='Rating', blank=False)
    date = models.DateField(verbose_name='Date', blank=False)

    class Meta(object):
        verbose_name = 'Exam Result'
        verbose_name_plural = 'Exam Results'

    def __unicode__(self):
        return '{}'.format(self.exam_id)
