from rest_framework import serializers
from .models import Sprint, Task


class SprintSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sprint
        # exposes all fields in the API
        fields = ('id', 'name', 'description', 'end', )


class TaskSerializer(serializers.ModelSerializer):

    assigned = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, required=False)
    status_display = serializers.SerializerMethodField('get_status_display')

    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'status', 'order',
                  'assigned', 'started', 'due', 'completed')

    def get_status_display(self, obj):
        return obj.get_status_display()
