from django.db import models
from django.utils import timezone


class Group(models.Model):
    scientific_name = models.CharField(max_length=50, null=True, unique=True)
    create_at = models.DateTimeField(editable=False, blank=True, default=timezone.now)

    pets = models.ForeignKey(
        "pets.Pet", null=True, related_name="Group", on_delete=models.DO_NOTHING
    )

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_at = timezone.now()

    def __repr__(self):
        return f"<[{self.id}] {self.scientific_name}>"
