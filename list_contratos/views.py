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
        # Extraia dados dos serializers relacionados e remova-os do contrato
        grupo_data = serializer.validated_data.pop("grupo_cliente")
        unidade_data = serializer.validated_data.pop("unidade_centro_de_custo")
        calendario_data = serializer.validated_data.pop("mes_calendario")
        # Primeiro, crie os registros relacionados e obtenha suas instâncias
        grupo = Grupo.objects.create(**grupo_data)
        unidade = Unidade.objects.create(**unidade_data)
        calendario = Calendario.objects.create(**calendario_data)
        # Agora, use essas instâncias ao criar o contrato
        created_contrato = Contrato.objects.create(
            grupo_cliente=grupo,
            unidade_centro_de_custo=unidade,
            mes_calendario=calendario,
            **serializer.validated_data
        )
        serializer = ContratoSerializer(instance=created_contrato)
        return Response(serializer.data, status.HTTP_201_CREATED)
