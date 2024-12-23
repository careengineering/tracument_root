# Generated by Django 5.0.6 on 2024-06-08 20:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Duty",
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
                ("name", models.CharField(max_length=200, unique=True)),
            ],
            options={"verbose_name": "Gorev", "verbose_name_plural": "Gorevler",},
        ),
        migrations.CreateModel(
            name="Payroll",
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
                ("name", models.CharField(max_length=200, unique=True)),
            ],
            options={"verbose_name": "Kadro", "verbose_name_plural": "Kadrolar",},
        ),
        migrations.CreateModel(
            name="Title",
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
                ("name", models.CharField(max_length=200, unique=True)),
            ],
            options={"verbose_name": "Unvan", "verbose_name_plural": "Unvanlar",},
        ),
        migrations.CreateModel(
            name="Unit",
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
                ("name", models.CharField(max_length=200, unique=True)),
            ],
            options={"verbose_name": "Birim", "verbose_name_plural": "Birimler",},
        ),
        migrations.CreateModel(
            name="Staff",
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
                ("name", models.CharField(max_length=200)),
                ("surname", models.CharField(max_length=200)),
                ("is_active", models.BooleanField(default=True)),
                ("duty", models.ManyToManyField(to="staff.duty")),
                (
                    "payroll",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="staff.payroll"
                    ),
                ),
                (
                    "title",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="staff.title"
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="staff.unit"
                    ),
                ),
            ],
            options={"verbose_name": "Personel", "verbose_name_plural": "Personeller",},
        ),
    ]
