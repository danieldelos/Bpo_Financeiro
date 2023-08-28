# from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status

class PersonView(APIView):
    def get(self, req: Request) -> Response:
        return Response ({"msg": "listagem feita"})
