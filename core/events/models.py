from django.db import models
from organiztion.models import Organization


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200, blank=True)
    organizations = models.ManyToManyField(Organization)
    image = models.ImageField(upload_to="events/", null=True)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"
        ordering = ["-date"]

    def __str__(self):
        return f"{self.image}"
