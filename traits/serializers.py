from rest_framework import serializers


class TraitSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    create_at = serializers.DateTimeField(read_only=True)
