from django.db import models
from django.utils.text import slugify


class Book(models.Model):
    name = models.CharField(max_length=30, unique=True)
    author = models.CharField(max_length=20)
    slug = slugify(name)

    def __str__(self) -> str:
        return self.name