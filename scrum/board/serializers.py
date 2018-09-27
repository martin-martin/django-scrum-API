from rest_framework import serializers
from .models import Sprint


class SprintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sprint
        # exposes all fields in the API
        fields = ('id', 'name', 'description', 'end', )
