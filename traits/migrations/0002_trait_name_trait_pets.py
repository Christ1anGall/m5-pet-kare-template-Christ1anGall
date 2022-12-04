# Generated by Django 4.1.3 on 2022-12-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0002_pet_age_pet_name_pet_sex_pet_weight"),
        ("traits", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="trait",
            name="name",
            field=models.CharField(default="Name", max_length=20, unique=True),
        ),
        migrations.AddField(
            model_name="trait",
            name="pets",
            field=models.ManyToManyField(related_name="Traits", to="pets.pet"),
        ),
    ]