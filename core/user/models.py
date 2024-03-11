from django.db import models
from django.contrib.auth.models import AbstractUser
from organiztion.models import Organization


class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=150)
    phone = models.PositiveBigIntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    organizations = models.ForeignKey(
        Organization, on_delete=models.SET_NULL, blank=True, null=True
    )

    USERNAME_FIELD = "username"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return f"{self.username}"
