from django.db import models

# Create your models here.
class Grupo(models.Model):
    grupo = models.CharField(max_length=20)

    def __repr__(self) -> str:
       return f"<Grupo: {self.id} - {self.grupo}>"    