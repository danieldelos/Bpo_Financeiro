from django.db import models
from list_calendario.models import Calendario
from list_grupos.models import Grupo
from list_unidades.models import Unidade


class Contrato(models.Model):
    LUCRO_REAL = "lucro_real"
    LUCRO_PRESUMIDO = "lucro_presumido"
    SIMPLES_NACIONAL = "simples_nacional"
    REGIME_TRIBUTARIO_CHOICES = [
        (LUCRO_REAL, "Lucro Real"),
        (LUCRO_PRESUMIDO, "Lucro Presumido"),
        (SIMPLES_NACIONAL, "Simples Nacional"),
    ]

    ATIVO = "ativo"
    INATIVO = "inativo"
    STATUS_CHOICES = [(ATIVO, "ativo"), (INATIVO, "inativo")]

    cliente_contrato = models.IntegerField()
    codigo = models.IntegerField()
    cnpj_cpf = models.CharField(max_length=14)
    grupo_cliente = models.ForeignKey(
        Grupo, on_delete=models.CASCADE, related_name="contratos"
    )
    razao_social = models.CharField(max_length=150)
    regime_tributario = models.CharField(
        max_length=20, choices=REGIME_TRIBUTARIO_CHOICES, default=LUCRO_REAL
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default=ATIVO)
    us = models.DecimalField(max_digits=10, decimal_places=2)
    unidade_centro_de_custo = models.ForeignKey(
        Unidade,
        on_delete=models.SET_NULL,
        null=True,
        related_name="contratos_centro_de_custo",
    )
    mes_calendario = models.ForeignKey(
        Calendario, on_delete=models.SET_NULL, null=True,
        related_name="contratos"
    )
    ano = models.IntegerField(null=True, blank=True)
    h_balanco = models.DecimalField(max_digits=10, decimal_places=2)
    dia_vencimento = models.IntegerField()
    pis = models.DecimalField(max_digits=10, decimal_places=2)
    cofins = models.DecimalField(max_digits=10, decimal_places=2)
    ir = models.DecimalField(max_digits=10, decimal_places=2)
    csll = models.DecimalField(max_digits=10, decimal_places=2)
    inss = models.DecimalField(max_digits=10, decimal_places=2)
    valor_liquido = models.DecimalField(max_digits=10, decimal_places=2)
    email = models.CharField(max_length=150)
    observacoes = models.TextField(null=True)

    def __repr__(self) -> str:
        return f"<cliente: {self.id} - {self.razao_social}>"
