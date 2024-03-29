from django.db import models
from django.utils import timezone


class Group(models.Model):
    scientific_name = models.CharField(max_length=50, unique=True)
    create_at = models.DateTimeField(editable=False, blank=True, default=timezone.now)

    pets = models.OneToOneField(
        "pets.Pet", related_name="group", on_delete=models.DO_NOTHING
    )



    def __repr__(self):
        return f"<[{self.id}] {self.scientific_name}>"
