# Generated by Django 4.2.4 on 2023-10-26 12:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("list_calendario", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="calendario",
            name="ano",
            field=models.IntegerField(null=True),
        ),
    ]
