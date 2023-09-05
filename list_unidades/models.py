from django.db import models


class Unidade(models.Model):
    centro_de_Custo = models.CharField(max_length=20)

    def __repr__(self) -> str:
        return f"<Centro_de_Custo: {self.id} - {self.centro_de_Custo}>"
