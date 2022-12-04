# Generated by Django 4.1.3 on 2022-12-04 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("groups", "0001_initial"),
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="pets",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="Group",
                to="pets.pet",
            ),
        ),
    ]