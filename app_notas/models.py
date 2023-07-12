from django.db import models

# Create your models here.
class Nota(models.Model):
    """
    Modelo que representa las notas del sistema
    """
    titulo = models.CharField(max_length=30)
    contenido = models.CharField(max_length=300)
    fecha = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo