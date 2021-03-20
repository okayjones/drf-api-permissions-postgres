from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'owner', 'name', 'description', 'done')
        model = Task