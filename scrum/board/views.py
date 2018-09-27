from rest_framework import authentication, permissions, viewsets
from .models import Sprint
from .serializers import SprintSerializer


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


# the ModelViewSet provides the necessary scaffolding for CRUD operations
# with the HTTP verbs we got to know. There's no need to define it here
# http://www.django-rest-framework.org/
# Make sure to inherit from both classes!
class SprintViewSet(DefaultsMixin, viewsets.ModelViewSet):
    """API endpoint for listening and creating sprints."""

    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer
