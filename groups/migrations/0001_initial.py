# Generated by Django 4.1.3 on 2022-12-04 21:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Group",
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
                    "scientific_name",
                    models.CharField(max_length=50, null=True, unique=True),
                ),
                (
                    "create_at",
                    models.DateTimeField(
                        blank=True, default=django.utils.timezone.now, editable=False
                    ),
                ),
            ],
        ),
    ]
