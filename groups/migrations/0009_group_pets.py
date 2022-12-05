# Generated by Django 4.1.3 on 2022-12-05 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0007_remove_pet_group"),
        ("groups", "0008_remove_group_pets"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="pets",
            field=models.OneToOneField(

                on_delete=django.db.models.deletion.CASCADE,
                related_name="pets",
                to="pets.pet",
            ),
            preserve_default=False,
        ),
    ]
