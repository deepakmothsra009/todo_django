from rest_framework import serializers

from .models import Task


# Task Serializer
class TaskSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        """
            Update the Task instance
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation

    class Meta:
        model = Task
        fields = "__all__"
