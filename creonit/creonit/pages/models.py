from django.db import models


# Create your models here.
class Pages(models.Model):
    name = models.CharField(max_length=100)

    slug = models.CharField(max_length=50, null=True, blank=True)

    url = models.CharField(max_length=200)

    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name
