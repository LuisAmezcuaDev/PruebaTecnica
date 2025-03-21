from django.db import models

# Create your models here.

class Tarea(models.Model):
    nombre = models.CharField(max_length=80)
    descripcion = models.TextField()
    estado = models.BooleanField(default=False)
