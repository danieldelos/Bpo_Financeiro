# Generated by Django 4.2.4 on 2023-09-04 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("list_unidades", "0001_initial"),
        ("list_grupos", "0001_initial"),
        ("list_calendario", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contrato",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cliente_contrato", models.IntegerField(max_length=10)),
                ("codigo", models.IntegerField(max_length=10)),
                ("cnpj_cpf", models.CharField(max_length=14)),
                ("razao_social", models.CharField(max_length=150)),
                (
                    "regime_tributario",
                    models.CharField(
                        choices=[
                            ("lucro_real", "Lucro Real"),
                            ("lucro_presumido", "Lucro Presumido"),
                            ("simples_nacional", "Simples Nacional"),
                        ],
                        default="lucro_real",
                        max_length=20,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("ativo", "ativo"), ("inativo", "inativo")],
                        default="ativo",
                        max_length=20,
                    ),
                ),
                ("us", models.DecimalField(decimal_places=2, max_digits=10)),
                ("h_balanco", models.DecimalField(decimal_places=2, max_digits=10)),
                ("dia_vencimento", models.IntegerField()),
                ("pis", models.DecimalField(decimal_places=2, max_digits=10)),
                ("cofins", models.DecimalField(decimal_places=2, max_digits=10)),
                ("ir", models.DecimalField(decimal_places=2, max_digits=10)),
                ("csll", models.DecimalField(decimal_places=2, max_digits=10)),
                ("inss", models.DecimalField(decimal_places=2, max_digits=10)),
                ("valor_liquido", models.DecimalField(decimal_places=2, max_digits=10)),
                ("email", models.CharField(max_length=150)),
                (
                    "grupo_cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="contratos",
                        to="list_grupos.grupo",
                    ),
                ),
                (
                    "mes_calendario",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="contratos",
                        to="list_calendario.calendario",
                    ),
                ),
                (
                    "unidade_centro_de_custo",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="contratos_centro_de_custo",
                        to="list_unidades.unidade",
                    ),
                ),
            ],
        ),
    ]
