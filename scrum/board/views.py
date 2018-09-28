from django.contrib.auth import get_user_model
from rest_framework import authentication, permissions, viewsets, filters
# changed in release 3.7.0 - import DjangoFilterBackend separately:
# https://github.com/encode/django-rest-framework/blob/22565d9a652fe45239c1480fd0acfc0d06ddda65/docs/topics/release-notes.md'
from django_filters.rest_framework import DjangoFilterBackend
from .forms import TaskFilter
from .models import Sprint, Task
from .serializers import SprintSerializer, TaskSerializer, UserSerializer


User = get_user_model()


class DefaultsMixin(object):
    """Default settings for view authentication, permissions, filtering
    and pagination."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100
    filter_backends = (
        DjangoFilterBackend,  # different import here!
        filters.SearchFilter,
        filters.OrderingFilter,
    )


# the ModelViewSet provides the necessary scaffolding for CRUD operations
# with the HTTP verbs we got to know. There's no need to define it here
# http://www.django-rest-framework.org/
# Make sure to inherit from both classes!
class SprintViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating sprints."""

    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer
    search_fields = ('name', )
    ordering_fields = ('end', 'name', )


class TaskViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listing and creating tasks."""

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_class = TaskFilter
    search_fields = ('name', 'description', )
    ordering_fields = ('name', 'order', 'started', 'due', 'completed', )


class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    """API endpoint for listing users."""

    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD, )
