from app_notas.models import Nota
from rest_framework import viewsets
from rest_framework.response import Response
from app_notas.serializadores import NotaSerializer

#Conjunto de Vistas para Administrar las Notas

class NotasViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite ver o editar notas.
    """
    queryset = Nota.objects.all().order_by('-fecha')
    serializer_class = NotaSerializer

