from django.db import models


class SexChoices(models.TextChoices):
    Male = "Male"
    Female = "Female"
    Not_Informed = "Not Informed"


class Pet(models.Model):
    name = models.CharField(max_length=50, null=False, default="Name")
    age = models.IntegerField(default=0)
    weight = models.FloatField(default=0)
    sex = models.CharField(
        max_length=20,
        default=SexChoices.Not_Informed,
        choices=SexChoices.choices,
    )

    traits = models.ManyToManyField("traits.Trait", related_name="Traits")

    def __repr__(self):
        return f"<[{self.id}]-{self.name} - {self.sex} - age: {self.age} >"
