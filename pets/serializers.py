from rest_framework import serializers
from groups.serializers import GroupSerializer
from traits.serializers import TraitSerializer
from .models import Pet
from traits.models import Trait
from groups.models import Group


class PetSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    weight = serializers.IntegerField()
    sex = serializers.CharField()
    group = GroupSerializer()
    traits = TraitSerializer(many=True)

    def create(self, validated_data: dict) -> Pet:

        traits_dict = validated_data.pop("traits")
        group_dict = validated_data.pop("group")

        pet_obj = Pet.objects.create(**validated_data)

        group_objt = Group.objects.get_or_create(**group_dict, pets=pet_obj)

        for traits in traits_dict:
            traits_obj = Trait.objects.get_or_create(**traits)

            pet_obj.traits.add(traits_obj[0])

        return pet_obj

    def update(self, instance: Pet, validated_data: dict):

        traits_dict: dict = validated_data.pop("trait", None)
        group_dict: dict = validated_data.pop("group", None)

        pet_obj, created = Pet.objects.get_or_create(pet=instance)

        if group_dict is not None:
            for key, value in group_dict.items():
                setattr(pet_obj, key, value)
            group_dict.save()

        if traits_dict is not None:
            for key, value in traits_dict.items():
                setattr(pet_obj, key, value)
            traits_dict.save()

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
