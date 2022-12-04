from rest_framework.views import APIView, Response, Request, status
from django.forms.models import model_to_dict
from .models import Group
from .serializers import GroupSerializer


class GroupView(APIView):
    def get(self, request: Request) -> Response:

        group = Group.objects.all()
    
        serializer = GroupSerializer(group, many=True)

        return Response(serializer.data)

        # return Response({"msg": "Rota Post Group"})

    def post(self, request: Request) -> Response:

        serializer = GroupSerializer(data=request.data)
        serializer.is_valid(raise_exceptions=True)
        serializer.save()

        """group = Group.objects.create(**serializer.validated_data)

        serializer = GroupSerializer(group)"""

        return Response(serializer.data, status.HTTP_201_CREATED)
