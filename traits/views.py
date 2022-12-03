from rest_framework.views import APIView, Response, Request, status
from django.forms.models import model_to_dict


class TraitsView(APIView):
    def get(self, request: Request) -> Response:
        return Response({"msg": "Rota GET Traits"}, status.HTTP_201_CREATED)
