from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Sprint(models.Model):
    """Development iteration period"""

    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    end = models.DateField(unique=True)

    def __str__(self):
        return self.name or _(f'Sprint ending {self.end}')


class Task(models.Model):
    """Unit of work to be done for the Sprint"""

    STATUS_DICT = {
        'TODO': 1,
        'IN_PROGRESS': 2,
        'TESTING': 3,
        'DONE': 4,
    }

    STATUS_CHOICES = (
        (STATUS_DICT['TODO'], _('Not Started')),
        (STATUS_DICT['IN_PROGRESS'], _('In Progress')),
        (STATUS_DICT['TESTING'], _('Testing')),
        (STATUS_DICT['DONE'], _('Done')),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    sprint = models.ForeignKey(Sprint, blank=True, null=True,
                               on_delete=models.DO_NOTHING)
    status = models.SmallIntegerField(choices=STATUS_CHOICES,
                                      default=STATUS_DICT['TODO'])
    order = models.SmallIntegerField(default=0)
    assigned = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 null=True, blank=True,
                                 on_delete=models.DO_NOTHING)
    started = models.DateField(blank=True, null=True)
    due = models.DateField(blank=True, null=True)
    completed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
