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
        group_obj = Group.objects.create(**group_dict)
        print('-' * 200)
        print(group_obj)
        print('-' * 200)
        pet = Pet.objects.create(**validated_data)

        """         for traits in traits_dict:
            traits_obj = Trait.objects.get_or_create(**traits)

            pet.traits.add(traits_obj[0])

        for group in group_dict:
            groups_obj = Group.objects.get_or_create(**group)

            pet.group.add(groups_obj[0]) """

        return pet

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
