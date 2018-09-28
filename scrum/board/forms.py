import django_filters
from .models import Task


class TaskFilter(django_filters.FitlerSet):

    class Meta:
        model = Task
        fields = ('sprint', 'status', 'assigned', )
