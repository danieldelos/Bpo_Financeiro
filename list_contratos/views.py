# from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from list_calendario.models import Calendario
from list_contratos.models import Contrato
from list_contratos.serializers import ContratoSerializer
from list_grupos.models import Grupo
from list_unidades.models import Unidade
import pandas as pd
from rest_framework.parsers import FileUploadParser
from django.shortcuts import get_object_or_404


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
            ano=calendario_data["ano"],
            **serializer.validated_data
        )
        serializer = ContratoSerializer(instance=created_contrato)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def get(self, req: Request) -> Response:
        contratoAll = Contrato.objects.all()
        serializer = ContratoSerializer(contratoAll, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class ContratoDetailView(APIView):
    def get(self, req: Request, id_contrato: int) -> Response:
        contrato = get_object_or_404(Contrato, id=id_contrato)
        serializer = ContratoSerializer(contrato)
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, req: Request, id_contrato: int) -> Response:
        contrato = get_object_or_404(Contrato, id=id_contrato)
        serializer = ContratoSerializer(data=req.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        for key, value in serializer.validated_data.items():
            setattr(contrato, key, value)
        contrato.save()
        serializer = ContratoSerializer(contrato)
        return Response(serializer.data)

    def delete(self, req: Request, id_contrato: int) -> Response:
        contrato = get_object_or_404(Contrato, id=id_contrato)
        contrato.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class UploadPlanilhaView(APIView):
    parser_class = (FileUploadParser,)

    def post(self, request):
        print(request.data)
        if 'file' not in request.data:
            return Response({"error": "No file was provided."}, status=status.HTTP_400_BAD_REQUEST)

        file = request.data['file']
        df = pd.read_excel(file, engine='openpyxl')
        
        for _, row in df.iterrows():
            # Aqui, processe cada linha da planilha e crie/altere os registros no banco de dados
            # Exemplo: 
            cliente_contrato = row['cliente_contrato']
            codigo = row['codigo']
            cnpj_cpf = row['cnpj_cpf']
            razao_social = row['razao_social']
            regime_tributario = row['regime_tributario']
            contract_status = row['status']
            us = row['us']
            h_balanco = row['h_balanco']
            dia_vencimento = row['dia_vencimento']
            pis = row['pis']
            cofins = row['cofins']
            ir = row['ir']
            csll = row['csll']
            inss = row['inss']
            valor_liquido = row['valor_liquido']
            email = row['email']
            grupo_cliente_id = row['grupo_cliente_id']
            mes_calendario_id = row['mes_calendario_id']
            unidade_centro_de_custo_id = row['unidade_centro_de_custo_id']
            observacoes = row['observacoes']

            # ... obtenha todos os outros campos

            # Verifique se já existe ou crie um novo, similar ao que fez anteriormente:
            grupo = Grupo.objects.get(id=grupo_cliente_id)
            calendario = Calendario.objects.get(id=mes_calendario_id)
            unidade = Unidade.objects.get(id=unidade_centro_de_custo_id)
            # ... e assim por diante para cada modelo

            Contrato.objects.create(
                cliente_contrato=cliente_contrato,
                codigo=codigo,
                cnpj_cpf=cnpj_cpf,
                razao_social=razao_social,
                regime_tributario=regime_tributario,
                status=contract_status,
                us=us,
                h_balanco=h_balanco,
                dia_vencimento=dia_vencimento,
                pis=pis,
                cofins=cofins,
                ir=ir,
                csll=csll,
                inss=inss,
                valor_liquido=valor_liquido,
                email=email,
                grupo_cliente=grupo,
                mes_calendario=calendario,
                unidade_centro_de_custo=unidade,
                observacoes=observacoes
                # ... defina todos os outros campos
            )

        return Response(status=status.HTTP_201_CREATED)