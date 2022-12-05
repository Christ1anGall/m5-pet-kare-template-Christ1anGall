from rest_framework import serializers
from .models import Group


class GroupSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    scientific_name = serializers.CharField(max_length=50)
    create_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        group = Group.objects.get_or_create(**validated_data)

        return group
