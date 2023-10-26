from django.db import models


class Calendario(models.Model):
    mes = models.CharField(max_length=30)
    ano = models.IntegerField(null=True)
    def __repr__(self) -> str:
        return f"<Competência: {self.id} - {self.mes}/{self.ano}>"
