# Generated by Django 4.1.3 on 2022-12-03 18:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("traits", "0002_trait_name_trait_pets"),
    ]

    operations = [
        migrations.AddField(
            model_name="trait",
            name="create_at",
            field=models.DateTimeField(
                blank=True, default=django.utils.timezone.now, editable=False
            ),
        ),
    ]
