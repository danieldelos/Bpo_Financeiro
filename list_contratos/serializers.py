from rest_framework import serializers
from list_calendario.serializers import CalendarioSerializer
from list_grupos.serializers import GrupoSerializer
from list_unidades.serializers import UnidadeSerializer


class ContratoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    cliente_contrato = serializers.IntegerField()
    codigo = serializers.IntegerField()
    cnpj_cpf = serializers.CharField(max_length=14)
    razao_social = serializers.CharField(max_length=150)

    grupo_cliente = GrupoSerializer()

    regime_tributario = serializers.CharField(max_length=20)
    status = serializers.CharField(max_length=20)
    us = serializers.DecimalField(max_digits=10, decimal_places=2)

    unidade_centro_de_custo = UnidadeSerializer()
    mes_calendario = CalendarioSerializer()
    ano = serializers.IntegerField(allow_null=True, required=False)

    h_balanco = serializers.DecimalField(max_digits=10, decimal_places=2)
    dia_vencimento = serializers.IntegerField()
    pis = serializers.DecimalField(max_digits=10, decimal_places=2)
    cofins = serializers.DecimalField(max_digits=10, decimal_places=2)
    ir = serializers.DecimalField(max_digits=10, decimal_places=2)
    csll = serializers.DecimalField(max_digits=10, decimal_places=2)
    inss = serializers.DecimalField(max_digits=10, decimal_places=2)
    valor_liquido = serializers.DecimalField(max_digits=10, decimal_places=2)
    email = serializers.CharField(max_length=150)
    observacoes = serializers.CharField()
