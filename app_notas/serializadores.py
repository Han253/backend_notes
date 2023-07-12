from app_notas.models import Nota
from rest_framework import serializers

class NotaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nota
        fields = ['id','titulo','contenido','fecha']