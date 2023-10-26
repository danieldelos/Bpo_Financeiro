from rest_framework import serializers


class CalendarioSerializer(serializers.Serializer):
    mes = serializers.CharField(max_length=30)
    ano = serializers.IntegerField(allow_null=True, required=False)
