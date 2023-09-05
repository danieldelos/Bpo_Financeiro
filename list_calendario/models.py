from django.db import models


class Calendario(models.Model):
    mes = models.CharField(max_length=30)

    def __repr__(self) -> str:
        return f"<Competência: {self.id} - {self.mes}>"
