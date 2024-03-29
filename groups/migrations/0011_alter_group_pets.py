# Generated by Django 4.1.3 on 2022-12-05 04:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0007_remove_pet_group"),
        ("groups", "0010_alter_group_pets"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="pets",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="group",
                to="pets.pet",
            ),
        ),
    ]
