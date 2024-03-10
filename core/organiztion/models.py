from django.db import models


class Organization(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200, blank=True)
    address = models.CharField(max_length=200)
    postcode = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Организация"
        verbose_name_plural = "Организации"
        ordering = ["title"]

    def __str__(self):
        return f"Организация - {self.title}. Адрес - {self.address}. Индекс  {self.postcode}"
