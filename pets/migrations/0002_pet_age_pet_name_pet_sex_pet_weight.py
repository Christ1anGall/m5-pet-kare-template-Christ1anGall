# Generated by Django 4.1.3 on 2022-12-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pets", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="pet",
            name="age",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="pet",
            name="name",
            field=models.CharField(default="Name", max_length=50),
        ),
        migrations.AddField(
            model_name="pet",
            name="sex",
            field=models.CharField(
                choices=[
                    ("Male", "Male"),
                    ("Female", "Female"),
                    ("Not Informed", "Not Informed"),
                ],
                default="Not Informed",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="pet",
            name="weight",
            field=models.FloatField(default=0),
        ),
    ]