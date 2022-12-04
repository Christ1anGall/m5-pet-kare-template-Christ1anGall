from django.db import models
from django.utils import timezone


class Trait(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False, default="Name")
    pets = models.ManyToManyField("pets.Pet", related_name="Traits")
    create_at = models.DateTimeField(editable=False, blank=True, default=timezone.now)

    def __repr__(self):
        return f"<[{self.id}] {self.name}>"
