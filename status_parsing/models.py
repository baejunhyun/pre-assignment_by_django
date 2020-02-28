from django.db import models


class PackageModel(models.Model):
    name = models.CharField(
        verbose_name="Package Name", max_length=100, default="", unique=True
    )
    depends = models.TextField(verbose_name="Dependencies", default="")
    description = models.TextField(verbose_name="Description", default="")
