from rest_framework import serializers


class GrupoSerializer(serializers.Serializer):
    grupo = serializers.CharField(max_length=20)
