# Generated by Django 4.2.12 on 2024-05-07 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("name", models.CharField(max_length=100)),
                ("manufacturer", models.CharField(max_length=100)),
                ("color", models.CharField(max_length=20)),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]