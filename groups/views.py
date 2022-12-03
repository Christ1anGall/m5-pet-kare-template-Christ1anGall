from rest_framework.views import APIView, Response, Request, status
from django.forms.models import model_to_dict


class GroupView(APIView):
    def get(self, request: Request) -> Response:
        return Response({"msg": "Rota Post Group"}, status.HTTP_201_CREATED)
