from rest_framework.views import APIView, Response, Request, status
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from .models import Pet
from serializers import PetSerializer


class PetsView(APIView):
    def post(self, request: Request) -> Response:
        serializer = PetSerializer(data=request.data)
        serializer.is_valid(raise_exceptions=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, request: Request, pet_id: int) -> Response:
        pets = get_object_or_404(Pet, id=pet_id)

        serializer = PetSerializer(pets)

        return Response(serializer.data)

    def patch(self, request: Request, pet_id: int):

        pets = get_object_or_404(Pet, id=pet_id)

        serializer = PetSerializer(pets, data=request.data, partial=True)
        serializer.is_valid(raise_exceptions=True)

        serializer.save()

        return Response(serializer.data)

        # return Response({"msg": "Rota GET Ptes"}, status.HTTP_201_CREATED)

    def delete(self, request: Request, pet_id: int) -> Response:
        pet = get_object_or_404(Pet, id=pet_id)
        pet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

        