# Generated by Django 4.2.4 on 2023-09-06 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("list_contratos", "0002_alter_contrato_cliente_contrato_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="contrato",
            name="observacoes",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
