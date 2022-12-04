from rest_framework import serializers
from ..groups.serializers import GroupsSerializer
from ..traits.serializers import TraitsSerializer


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.IntegerField()
    sex = serializers.CharField()
    groups = GroupsSerializer(many=True, read_only=True)
    traits = TraitsSerializer(many=True, read_only=True)
