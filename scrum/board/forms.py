import django_filters
from django.contrib.auth import get_user_model
from .models import Task, Sprint


User = get_user_model()


class NullFilter(django_filters.BooleanFilter):
    """Filter on a field set as null or not."""

    def filter(self, qs, value):
        if value is not None:
            # attention: see changes in comment below ('field_name')
            return qs.filter(**{f'{self.field_name}__isnull': value})
        return qs


class SprintFilter(django_filters.FilterSet):

    # attention: changed to 'lookup_expr'
    # https://django-filter.readthedocs.io/en/master/ref/filters.html
    end_min = django_filters.DateFilter(field_name='end', lookup_expr='gte')
    end_max = django_filters.DateFilter(field_name='end', lookup_expr='lte')

    class Meta:
        model = Sprint
        fields = ('end_min', 'end_max', )


class TaskFilter(django_filters.FilterSet):

    # django-filters 2.0 has changed 'name' to 'field_name'!
    # https://django-filter.readthedocs.io/en/master/guide/migration.html#filter-name-renamed-to-filter-field-name-792
    backlog = NullFilter(field_name='sprint')

    class Meta:
        model = Task
        fields = ('sprint', 'status', 'assigned', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['assigned'].extra.update(
            {'to_field_name': User.USERNAME_FIELD})
