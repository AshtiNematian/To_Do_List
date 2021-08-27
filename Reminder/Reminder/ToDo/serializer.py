from rest_framework import serializers

from ToDo.models import Task


class TaskSerrializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
