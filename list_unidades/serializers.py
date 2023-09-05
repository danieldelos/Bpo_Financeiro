from rest_framework import serializers


class UnidadeSerializer(serializers.Serializer):
    centro_de_Custo = serializers.CharField(max_length=20)
