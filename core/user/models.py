from django.db import models
from organiztion.models import Organization


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    phone = models.PositiveBigIntegerField(blank=True, null=True)
    company = models.ForeignKey(
        Organization, on_delete=models.CASCADE, blank=True, null=True
    )
