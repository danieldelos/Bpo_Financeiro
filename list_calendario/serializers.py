from rest_framework import serializers


class CalendarioSerializer(serializers.Serializer):
    mes = serializers.CharField(max_length=30)
