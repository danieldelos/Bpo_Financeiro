# from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from list_calendario.models import Calendario
from list_contratos.models import Contrato
from list_contratos.serializers import ContratoSerializer
from list_grupos.models import Grupo
from list_unidades.models import Unidade


class ContratoView(APIView):
    def post(self, req: Request) -> Response:
        serializer = ContratoSerializer(data=req.data)
        if not serializer.is_valid():
            return Response(serializer.errors)
        # Extrai dados dos serializers relacionados e remove do contrato
        grupo_data = serializer.validated_data.pop("grupo_cliente")
        unidade_data = serializer.validated_data.pop("unidade_centro_de_custo")
        calendario_data = serializer.validated_data.pop("mes_calendario")

        # Verifique se já existe ou crie um novo
        grupo, _ = Grupo.objects.get_or_create(**grupo_data)
        unidade, _ = Unidade.objects.get_or_create(**unidade_data)
        calendario, _ = Calendario.objects.get_or_create(**calendario_data)

        # Agora, use essas instâncias ao criar o contrato
        created_contrato = Contrato.objects.create(
            grupo_cliente=grupo,
            unidade_centro_de_custo=unidade,
            mes_calendario=calendario,
            **serializer.validated_data
        )
        serializer = ContratoSerializer(instance=created_contrato)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        contratoAll = Contrato.objects.all()
        serializer = ContratoSerializer(contratoAll, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

class ContratoDetailView(APIView):
    def get(self, req: Request, id_contrato) -> Response:
        ...