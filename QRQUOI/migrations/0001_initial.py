# Generated by Django 5.0.6 on 2024-06-09 00:01

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Utilisateur",
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
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("nom", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("DateInscription", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
