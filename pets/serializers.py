from rest_framework import serializers
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.IntegerField()
    sex = serializers.CharField()
    groups = GroupSerializer(many=True, read_only=True)
    traits = TraitSerializer(many=True, read_only=True)
